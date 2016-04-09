import sys
varnames = []
removedvars = {}
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
		thevalues = l.strip().split(" ")
		removedvars[thevalues[0]] = thevalues[1]
with open(sys.argv[1], "r") as infile:
	foundit = False
	for l in infile:
		if foundit:
			parts = l.strip().split(" ")
			i = 0
			for varname in varnames:
				if varname in removedvars:
					print(varname, removedvars[varname])
				else:
					print(varname, parts[i])
					i += 1
			break
		else:
			if "New solution" in l:
				foundit = True
