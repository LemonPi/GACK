class Variable:
	def __init__(self, name, domain):
		self.name = name
		self.domain = domain

colorRed = 0
colorOrange = 1
colorYellow = 2
colorGreen = 3
colorBlue = 4
colorViolet = 5

colorsDom = [0, 1, 2, 3, 4, 5] # roygbv
heightDom = [0, 1, 2, 3, 4]

class Cell:
	"""represent a spacial region with all the plant properties that are allowed there"""

	def __init__(self, index, area, nat_shading, view_dist, adj=None):
		if adj == None:
			adj = []
		# immutable properties of the space (so they are values rather than Varible objects)
		self.index = index
		self.area = area
		# natural shading not counting for the effect of neighbouring plants (only the effect of location)
		self.nat_shading = nat_shading

		# number of edges between it and a walking area, so view_dist = 0 means it's adjacent to a walking area
		self.view_dist = view_dist

		# neighbouring cells
		self.adj = adj


		# mutable Variables of the space that should have their domains pruned
		self.variables = []
		self.add_var(Variable("moist", [0, 1, 2, 3]))
		self.add_var(Variable("color_spring", list(colorsDom)))
		self.add_var(Variable("color_summer", list(colorsDom)))
		self.add_var(Variable("color_fall", list(colorsDom)))
		self.add_var(Variable("height", list(heightDom)))

	def add_neighbour(self, neighbour):
		"""shoulder only be done during initialization; neighbour is another cell object"""
		self.adj.append(neighbour)

	def add_var(self, var):
		self.variables.append(var)
	def get_var(self, varname):
		for var in self.variables:
			if var.name == varname:
				return var
		return var

	def __repr__(self):
		return "Cell(index={},area={},nat_shading={},view_dist={}, adj_count={})".format(
			self.index, self.area, self.nat_shading, self.view_dist, len(self.adj))

def addneighbour2way(a, b):
	if b not in a.adj:
		a.add_neighbour(b)
	if a not in b.adj:
		b.add_neighbour(a)

def flood(startcell, dist):
	newdist = dist + 1
	for adjcell in startcell.adj:
		if newdist < adjcell.view_dist:
			adjcell.view_dist = newdist
			flood(adjcell, newdist)

def buildcells():
	cells = [Cell(0, 0, 0, -1)]
	with open("cell_areas.txt", "r") as infile:
		indata = [int(b) for b in infile.read().strip().split(",")]
		for cellarea in indata:
			# we do not account for natural shading yet
			cells.append(Cell(len(cells), cellarea, 0, 9999)) 
	with open("adjacent.csv", "r") as infile:
		for l in infile:
			a = [int(b) for b in l.strip().split(",")]
			cell = cells[a[0]]
			for neighbor in sorted(a[1:]):
				addneighbour2way(cell, cells[neighbor])
	# flood fill for view dist
	# yeah I know this is wrong
	flood(cells[0], -1)
	return cells

def writealladjclause(cells, flowertypes, outfile):
	print("Gack", file=outfile)
	for cell in cells:
		if cell.index == 0:
			continue
		for var in cell.variables:
			print("cell{}_{} {}".format(cell.index, 
				var.name, " ".join(str(a) for a in var.domain)),
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
			# 0, 1, 2
			# so maximum difference must be < 2
			print("hard(abs(cell{}_moist - cell{}_moist) < 2)".
				format(cell.index, adj.index), file=outfile)
			if adj.view_dist != cell.view_dist:
				print("hard(cell{}_height {} cell{}_height)".format(cell.index,
	"<=" if cell.view_dist < adj.view_dist else ">=",
	adj.index), file=outfile)
			print("soft(1, (cell{}_color_spring != cell{}_color_spring)|| (cell{}_color_summer != cell{}_color_summer) || (cell{}_color_fall != cell{}_color_fall))".format(cell.index, adj.index,
				cell.index, adj.index,
				cell.index, adj.index), file=outfile)
	# no color should take up more than 3/4 of the garden
	if False:#for color in colorsDom:
		for season in ["spring", "summer", "fall"]:
			print("(count {} ({}) lt {})".format(
				color,
				" ".join("cell{}_color_{}".format(cell.index, season)
					for cell in cells if cell.index != 0),
				int((len(cells) - 1)*2/3)), file=outfile)

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
			if len(var.domain) != 1:
				continue
			print("cell{}_{} {}".format(cell.index, 
				var.name, " ".join(str(a) for a in var.domain)),
			file=outfile)
def main():
	cells = buildcells()
	flowertypes = readflowertypes()
	cells[3].get_var("color_summer").domain = [0] # red in summer
	with open("theoutfile.txt", "w") as outfile:
		writealladjclause(cells, flowertypes, outfile)
	with open("removedvars.txt", "w") as outfile:
		writeremovedvars(cells, outfile)

if __name__ == "__main__":
	main()
