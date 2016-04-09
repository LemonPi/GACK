import sys
varnames = []
with open("theoutfile.txt", "r") as infile:
	firstline = True
	for l in infile:
		if firstline:
			firstline = False
			continue
		if "(" in l:
			continue
		varnames.append(l.strip().split(" ")[0])
with open("removedvars.txt", "r") as infile:
	for l in infile:
		varnames.remove(l.strip().split(" ")[0])
with open(sys.argv[1], "r") as infile:
	foundit = False
	for l in infile:
		if foundit:
			parts = l.strip().split(" ")
			for i in range(len(parts)):
				print(varnames[i], parts[i])
			break
		else:
			if "New solution" in l:
				foundit = True
