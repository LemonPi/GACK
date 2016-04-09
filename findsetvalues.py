import pickle
def doit(plants, key):
	existing = {}
	for plant in plants:
		a = plant[key]
		for k in a:
			ss = set(a[k])
			if k in existing:
				existing[k].update(ss)
			else:
				existing[k] = ss
	return existing
def dprint(a):
	for k in a:
		print("===", k, "===")
		print(",".join(a[k]))

with open("allplants.bin", "rb") as infile:
	allplants = pickle.load(infile)
dprint(doit(allplants, "char"))
dprint(doit(allplants, "cond"))