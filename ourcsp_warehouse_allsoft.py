from cspbase import *
from propagators import *

def sat_implies_2(vara, middle, varb, end):
	output = []
	for i in vara.dom:
		for j in varb.dom:
			if not ((i == middle) != False and (j == end) == False):
				output.append((i, j))
	return output

def main():
	# port of warehouse.cp in Toulbar2's verification/default folder
	numWarehouse = 5
	numStore = 10
	openCost = 30
	costs = [
		[20, 24, 11, 25, 30],
		[28, 27, 82, 83, 74],
		[74, 97, 71, 96, 70],
		[2, 55, 73, 69, 61],
		[46, 96, 59, 83, 4],
		[42, 22, 29, 67, 59],
		[1, 5, 73, 59, 56],
		[10, 73, 13, 43, 96],
		[93, 35, 63, 85, 46],
		[47, 65, 55, 71, 95]
	]
	# warehouse open state
	warehouses = [Variable("warehouse" + str(i), [0, 1]) for i in range(numWarehouse)]
	warehouseOpeningCosts = [SoftConstraint("openingcost" + str(i), [warehouses[i]], lambda a: 0 if a == 0 else openCost, mc=openCost) for i in range(numWarehouse)]

	stores = [Variable("store" + str(i), [0, 1, 2, 3, 4]) for i in range(numStore)]
	storeChanneling = [None] * numStore * numWarehouse;
	i = 0
	for warehouse in range(numWarehouse):
		for store in range(numStore):
			constraint = SoftConstraint("channeling" + str(store) + "-" + str(warehouse), [stores[store], warehouses[warehouse]], lambda i, j, middle=warehouse: 0 if not ((i == middle) != False and (j == 1) == False) else 10000, mc=10000)
			storeChanneling[i] = constraint;
			i += 1
	storeTransportation = [SoftConstraint("trans" + str(store), [stores[store]], lambda a, store=store: costs[store][a], mc=max(costs[store])) for store in range(numStore)]

	csp = SCSP("warehouse", warehouses + stores)
	for constraint in storeChanneling:
		csp.add_soft_constraint(constraint)
	for constraint in warehouseOpeningCosts:
		csp.add_soft_constraint(constraint)
	for constraint in storeTransportation:
		csp.add_soft_constraint(constraint)

    # upper bound of 500
	bb = BB(csp, UB=500)
	#bb.trace_on()
	bb.bb_search(prop_GAC)
	
main()
