orbitFrom = []
orbitTo = []
orbitDist = {}

fp = open("input_1.txt", "r")
lines = fp.readlines()
print(f"Read {len(lines)} lines")
for line in lines:
    line = line.strip()
    if not line: break
    vals = line.split(")")
    # print(f"    vals={vals}")
    orbitFrom.append(vals[0])
    orbitTo.append(vals[1])

print(f"Using {len(orbitFrom)} orbits")
orbitDist["COM"] = 0
queue = ["COM"]
while(queue):
    fromName = queue.pop(0)
    for i in range(0, len(orbitFrom)):
        if(orbitFrom[i] == fromName):
            toName = orbitTo[i]
            print(f"   {fromName} ) {toName}: hasDist={fromName in orbitDist}")
            orbitDist[toName] = orbitDist[fromName] + 1
            queue.append(toName)

totalDist = 0
for aDist in orbitDist.values():
    totalDist += aDist

# print(f"MAP_FROM: {orbitFrom}")
# print(f"MAP_TO  : {orbitTo}")
# print(f"DIST: {orbitDist}")
print(f"TOTAL: {totalDist}")
