import sys
varnames = []
vardoms = []
removedvars = {}
with open("theoutfile.txt", "r") as infile:
	firstline = True
	for l in infile:
		if firstline:
			firstline = False
			continue
		if "(" in l:
			continue
		varline = l.strip().split(" ")
		varnames.append(varline[0])
		vardoms.append(varline[1:])
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
			for vari in range(len(varnames)):
				varname = varnames[vari]
				if varname in removedvars:
					print(varname, removedvars[varname])
				else:
					print(varname, vardoms[vari][int(parts[i])])
					i += 1
			break
		else:
			if "New solution" in l:
				foundit = True
