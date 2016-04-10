import sys
sys.path.append("../")
from cell import *
def writealladjclause(cells, flowertypes, cellwidths, prefs, outfile):
	print("Gack", file=outfile)
	for cell in cells:
		if cell.index == 0:
			continue
		for var in cell.variables:
			print("cell{}_{} {}".format(cell.index, 
				var.name, " ".join(str(a) for a in var.dom)),
			file=outfile)
	for cell in cells:
		if cell.index == 0:
			continue
		doprintflowers(cell.index, flowertypes, cellwidths[cell.index - 1], cell.view_dist, outfile)
		for adj in cell.adj:
			if adj.index > cell.index:
				continue
			if adj.index == 0:
				continue
			# soil must be similar
			# 0 dry, 1 average, 2 moist, 3 wet
			# so maximum difference must be < 2
			print("hard(abs(cell{}_moist - cell{}_moist) < 2)".
				format(cell.index, adj.index), file=outfile)
			# no blocking:
			# adjacent with smaller view_dist should have smaller or equal height
			if adj.view_dist != cell.view_dist:
				print("hard(cell{}_height {} cell{}_height)".format(cell.index,
	"<=" if cell.view_dist < adj.view_dist else ">=",
	adj.index), file=outfile)
			# adjacent should have different colour in either spring, summer, or fall
			#print("soft(4, (cell{}_color_spring != cell{}_color_spring)|| (cell{}_color_summer != cell{}_color_summer) || (cell{}_color_fall != cell{}_color_fall))".format(cell.index, adj.index,
			#	cell.index, adj.index,
			#	cell.index, adj.index), file=outfile)
			#print("soft(1, (cell{}_color_spring != 3) != (cell{}_color_spring != 3))".format(cell.index, adj.index), file=outfile);
			print("soft({}, (cell{}_color_spring != cell{}_color_spring))".format(prefs["season_weight_spring"], cell.index, adj.index), file=outfile)
			print("soft({}, (cell{}_color_summer != cell{}_color_summer))".format(prefs["season_weight_summer"], cell.index, adj.index), file=outfile)
			print("soft({}, (cell{}_color_fall != cell{}_color_fall))".format(prefs["season_weight_fall"], cell.index, adj.index), file=outfile)

def readflowertypes():
	flowers = []
	with open("flowertypes.csv", "r") as infile:
		a = True
		for l in infile:
			if a:
				a = False
				continue #skip first
			b = [int(b) for b in l.strip().split(",")]
			# height, color, season, moisture
			outflower = {
				"height": b[0],
				"color_spring": b[1] if b[2] == 0 else colorGreen,
				"color_summer": b[1] if b[2] == 1 else colorGreen,
				"color_fall": b[1] if b[2] == 2 else colorGreen,
				"moist": b[3],
				"-spread": b[4],
				"-traffic": b[5],
			}
			flowers.append(outflower)
	return flowers
def doprintflowers(cellindex, flowertypes, cellwidth, cell_view_dist, outfile):
	# cell must have properties corresponding to a valid flower type
	theset = set()
	allflower = []
	satisfying = {}
	varnames = [a for a in flowertypes[0] if a[0] != "-"]
	for flower in flowertypes:
		firstvname = True
		myspread = flower["-spread"]
		if myspread > cellwidth:
			continue
		lowtraffic = flower["-traffic"] <= 1
		if lowtraffic and cell_view_dist <= 0:
			continue
		flowertuple = tuple(flower[a] for a in flower if a[0] != "-")
		if flowertuple in theset:
			continue
		theset.add(flowertuple)
		for i in range(len(flowertuple)):
			for j in range(i + 1, len(flowertuple)):
				myval = (i, j)
				fv = (flowertuple[i], flowertuple[j])
				if not myval in satisfying:
					satisfying[myval] = set([fv])
				else:
					satisfying[myval].add(fv)
	firstsatisfy = True
	for fv in satisfying:
		print("hard(", end="", file=outfile)
		firstvname = True
		for ft in satisfying[fv]:
			if firstvname:
				firstvname = False
			else:
				print("||", end="", file=outfile)
			print("(cell{}_{} == {} && cell{}_{} == {})".format(
				cellindex, varnames[fv[0]], ft[0],
				cellindex, varnames[fv[1]], ft[1]),
				end="", file=outfile)
		print(")", file=outfile)
def writeremovedvars(cells, outfile):
	for cell in cells:
		if cell.index == 0:
			continue
		for var in cell.variables:
			if len(var.dom) != 1:
				continue
			print("cell{}_{} {}".format(cell.index, 
				var.name, " ".join(str(a) for a in var.dom)),
			file=outfile)

def readwidths():
	# height of flowerbed is 25ft = 762 cm, height is 790px
	px2cm = 762 / 790
	with open("cellwidths.csv", "r") as infile:
		return [int(int(i)*px2cm) for i in infile.read().strip().split(",")]

def readprefs():
	with open("user_prefs.txt", "r") as infile:
		return [a.split() for a in infile.read().strip().split("\n") if not (len(a) == 0 or a[0] == "#")]

def applyprefs(cells, userprefs):
	outprefs = {}
	for pref in userprefs:
		if pref[0] == "color_rank":
			pval = [int(i) for i in pref[1:]]
			# check that all colours are represented
			for i in range(len(colorsDom)):
				if not i in pval:
					print("color_rank is missing", i)
					break
			else:
				print("setting all domains")
				for cell in cells:
					for colordom in ["color_spring", "color_summer", "color_fall"]:
						cell.get_var(colordom).dom = list(pval)
		elif pref[0] == "season_rank":
			seasons = pref[1:]
			if len(seasons) != 3:
				print("seasons weight length is wrong")
			else:
				for i in range(3):
					weight = 3 - i
					outprefs["season_weight_" + seasons[i]] = weight
	# apply colour forcings - must be done last since these domain changes have priority
	for pref in userprefs:
		if pref[0].startswith("cell_force_"):
			punch = pref[0][len("cell_force_"):].split("_", 2)
			cell = cells[int(punch[0])]
			cell.get_var("color_" + punch[1]).dom = list([int(a) for a in pref[1:]])
	return outprefs
def main():
	# build the graph of cells
	cells = buildcells()
	# read the valid flower types from the csv
	flowertypes = readflowertypes()
	# read the cell widths (calculated using oriented minimum bounding box) from the csv
	cellwidths = readwidths()
	# read and apply user preferences
	userprefs = readprefs()
	outprefs = applyprefs(cells, userprefs)
	# write ToulBar cp output
	with open("theoutfile.txt", "w") as outfile:
		writealladjclause(cells, flowertypes, cellwidths, outprefs, outfile)
	# Write list of all variables with domain size=1 (which ToulBar omits) for result display
	with open("removedvars.txt", "w") as outfile:
		writeremovedvars(cells, outfile)

if __name__ == "__main__":
	main()
