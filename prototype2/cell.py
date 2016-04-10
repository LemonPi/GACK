import os
from cspbase import Variable
colorRed = 0
colorOrange = 1
colorYellow = 2
colorGreen = 3
colorBlue = 4
colorViolet = 5

colorsDom = [0, 1, 2, 3, 4, 5] # roygbv
colorsDom.reverse()
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
		self.add_var(Variable("color_spring", colorsDom))
		self.add_var(Variable("color_summer", colorsDom))
		self.add_var(Variable("color_fall", colorsDom))
		self.add_var(Variable("height", heightDom))

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
	with open(os.path.join(os.path.dirname(__file__), "../cell_areas.txt"), "r") as infile:
		indata = [int(b) for b in infile.read().strip().split(",")]
		for cellarea in indata:
			# we do not account for natural shading yet
			cells.append(Cell(len(cells), cellarea, 0, 9999)) 
	with open(os.path.join(os.path.dirname(__file__), "../adjacent.csv"), "r") as infile:
		for l in infile:
			a = [int(b) for b in l.strip().split(",")]
			cell = cells[a[0]]
			for neighbor in sorted(a[1:]):
				addneighbour2way(cell, cells[neighbor])
	# flood fill for view dist
	# yeah I know this is wrong
	flood(cells[0], -1)
	return cells
