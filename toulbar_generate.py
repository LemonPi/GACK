from cell import *
def writealladjclause(cells, flowertypes, outfile):
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
		doprintflowers(cell.index, flowertypes, outfile)
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
			print("soft(1, (cell{}_color_spring != cell{}_color_spring)|| (cell{}_color_summer != cell{}_color_summer) || (cell{}_color_fall != cell{}_color_fall))".format(cell.index, adj.index,
				cell.index, adj.index,
				cell.index, adj.index), file=outfile)

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
				"moist": b[3]
			}
			flowers.append(outflower)
	return flowers
def doprintflowers(cellindex, flowertypes, outfile):
	# cell must have properties corresponding to a valid flower type
	print("hard(", end="", file=outfile)
	firstflower = True
	for flower in flowertypes:
		if firstflower:
			firstflower = False
		else:
			print("||", end="", file=outfile)
		print("(", end="", file=outfile)
		firstvname = True
		for vname in flower:
			if firstvname:
				firstvname = False
			else:
				print("&&", end="", file=outfile)
			print("(cell{}_{} == {})".format(
				cellindex, vname, flower[vname]),
				end="", file=outfile)
		print(")", end="", file=outfile)
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
def main():
	# build the graph of cells
	cells = buildcells()
	# read the valid flower types from the csv
	flowertypes = readflowertypes()
	# set user preferences
	cells[3].get_var("color_summer").dom = [0] # red in summer
	# write ToulBar cp output
	with open("theoutfile.txt", "w") as outfile:
		writealladjclause(cells, flowertypes, outfile)
	# Write list of all variables with domain size=1 (which ToulBar omits) for result display
	with open("removedvars.txt", "w") as outfile:
		writeremovedvars(cells, outfile)

if __name__ == "__main__":
	main()
