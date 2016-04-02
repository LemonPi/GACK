
class Cell:
	"""represent a spacial region with all the plant properties that are allowed there"""

	def __init__(self, index, area, nat_shading, view_dist, adj=[]):
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



	def add_neighbour(self, neighbour):
		"""shoulder only be done during initialization; neighbour is another cell object"""
		self.adj.append(neighbour)

