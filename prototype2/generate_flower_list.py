import sys
sys.path.append("../")
import pickle
from cell import *
from generate_valid_plant_classes import *
from toulbar_generate import readwidths

def generate_plant_reverse_mapping():
	plantmap = {}
	with open("../allplants.bin", "rb") as infile:
		allplants = pickle.load(infile)
	for plant in allplants:
		outplant = cleanup(plant)
		planttuple = planttotuple(outplant)[:-2]
		# cut out spread and traffic.
		if planttuple in plantmap:
			plantmap[planttuple].append(outplant)
		else:
			plantmap[planttuple] = [outplant]
	return plantmap

def get_cell_targets(cells, plantmap, cellwidths, outfile):
	solutionout = {}
	with open("solutionout.txt", "r") as infile:
		for l in infile:
			l = l.strip().split(" ", 2)
			solutionout[l[0]] = int(l[1])
	for cell in range(1, len(cells)):
		cs = "cell" + str(cell) + "_"
		cellwidth = cellwidths[cell - 1]
		cell_view_dist = cells[cell].view_dist
		floweringseason = 0
		thecolor = colorGreen
		# this may not roundtrip for plants that never bloom
		# need to figure that out...
		seasons = ["spring", "summer", "fall"]
		for seasoni in range(len(seasons)):
			season = seasons[seasoni]
			if solutionout[cs + "color_" + season] != colorGreen:
				floweringseason = seasoni
				thecolor = solutionout[cs + "color_" + season]
		cell_planttuple = (
			solutionout[cs + "height"],
			thecolor,
			floweringseason,
			solutionout[cs + "moist"])
		if cell_planttuple in plantmap:
			plants = plantmap[cell_planttuple]
		else:
			plants = []
		usableplants = []
		for plant in plants:
			# logic duplicated from toulbar_generate.
			if plant["spread"] > cellwidth:
				continue
			lowtraffic = plant["traffic"] <= 1
			if lowtraffic and cell_view_dist <= 0:
				continue
			usableplants.append(plant["name"] + "@" + plant["common"])
		print("Cell" + str(cell) + ":" + "|".join(usableplants), file=outfile)

def main():
	plantmap = generate_plant_reverse_mapping()
	cells = buildcells()
	cellwidths = readwidths()
	with open("plant_choices.txt", "w", encoding="utf-8") as outfile:
		targetcelltuples = get_cell_targets(cells, plantmap, cellwidths, outfile)

if __name__ == "__main__":
	main()
