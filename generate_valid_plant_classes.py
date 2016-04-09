import pickle

# height 0 = 0-30cm; 1 = 30-60cm, 2 = 60-90cm, 3 = 90 - 120cm; 4 = >120cm

def calcheight(plant):
	a = plant["char"]["Height"]
	for b in a:
		if not b.endswith("cm"):
			continue
		c = [int(d) for d in b[0:b.find(" ")].split("-")]
		avgheight = sum(c) / 2
		for i in range(4):
			if avgheight < (i*30 + 30):
				return i
		return 4

def calccolor(plant):
	colortable = {
		"Light Pink": 0, # red
		"Mauve/Lilac": 5, # violet
		"Black": 5, # violet
		"Salmon": 0, # red
		"Orange": 1, # orange
		"Deep Pink": 0, # red
		"Mixed": 5, # violet
		"Red": 0,
		"Gold": 2,
		"Green": 3,
		"Brown": 2,
		"Deep Blue": 4,
		"Purple": 5,
		"Light Blue": 4,
		"Creamy Yellow": 2,
		"White": 2, # yellow
		"Yellow": 2,
	}
	for color in plant["char"]["Flower Colour"]:
		if color in colortable:
			return colortable[color]
	return 5 # whatever, violet

def calcseason(plant):
	for time in plant["char"]["Blooming Time"]:
		mytimes = ["Spring", "Summer", "Fall", "Winter"]
		for i in range(4):
			if mytimes[i] in time:
				return i
	return 1 # summer

def calcph(plant):
	phs = ["Acid", "Neutral", "Alkaline"]
	print(plant["cond"]["Soil pH"])
	for phthing in plant["cond"]["Soil pH"]:
		for i in range(3):
			if phs[i] == phthing:
				return i
	return 1 # neutral

def calcmoisture(plant):
	thing = plant["cond"]["Soil Moisture"][-1]
	moisture = ["Dry", "Average", "Moist", "Wet"]
	for i in range(4):
		if moisture[i] == thing:
			return i
	return 1 # average

def cleanup(plant):
	outplant = {
		"name": plant["name"],
		"plantnum": plant["plantnum"],
		"common": plant["common"],
		"height": calcheight(plant),
		"color": calccolor(plant),
		#"ph": calcph(plant),
		"moisture": calcmoisture(plant),
		"season": calcseason(plant)
	}
	return outplant

def planttotuple(plant):
	return (plant["height"], plant["color"], plant["season"], plant["moisture"])

with open("allplants.bin", "rb") as infile:
	allplants = pickle.load(infile)
newplants = [cleanup(plant) for plant in allplants]
plantset = set()
for plant in newplants:
	plantset.add(planttotuple(plant))
print("Height,Color,Season,Moisture")
for plant in plantset:
	print(",".join(str(a) for a in plant))
#with open("newplants.bin", "wb") as outfile:
#	pickle.dump(newplants, outfile)
