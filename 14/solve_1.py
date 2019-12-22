import math
import sys
# import cvxpy
# import numpy as np

fp = open("input.txt", "r")
lines = fp.readlines()
print(f"input has {len(lines)} lines")


# Read in chem balances



oreCounts = {}

for line in lines:
    line = line.strip()
    if(len(line) == 0): break
    lhs, rhs = list(map(str.strip, line.split("=>")))


    lhsChemStrs = list(map(str.strip, lhs.split(",")))
    lhsChems = []
    for lhsChem in lhsChemStrs:
        amt, chem = lhsChem.split(" ")
        lhsChems.append((int(amt), chem))
    lhsBal

    rhsAmt, rhsChem = rhs.split(" ")
    rhsAmt = int(rhsAmt)
    balances.append({ 'lhs': lhsChems, 'rhs': (rhsAmt, rhsChem)})

print(f"All chems: {allChems}")
print(f"{len(balances)} Balances:")
for bal in balances:
    print(f"  {bal['lhs']} => {bal['rhs']}")
