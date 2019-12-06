orbitFrom = []
orbitTo = []
orbitDist = {}

fp = open("input_2.txt", "r")
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
            # print(f"   {fromName} ) {toName}: hasDist={fromName in orbitDist}")
            orbitDist[toName] = orbitDist[fromName] + 1
            queue.append(toName)


def getOrbitPath(toName):
    fromName = orbitFrom[orbitTo.index(toName)]
    if(fromName == "COM"):
        return fromName
    else:
        return fromName + " " + getOrbitPath(fromName)

youPath = getOrbitPath("YOU").split(" ")[::-1]
# print(f"youPath={youPath}")
sanPath = getOrbitPath("SAN").split(" ")[::-1]
# print(f"sanPath={sanPath}")

sameIdx = 0
for i in range(0, min(len(youPath), len(sanPath))):
    if(youPath[i] == sanPath[i]):
        sameIdx += 1
    else:
        break
youPath = youPath[sameIdx:]
sanPath = sanPath[sameIdx:]

print(f"youPath={youPath}")
print(f"sanPath={sanPath}")
print(f"totalPathLen={len(youPath) + len(sanPath)}")

# print(f"MAP_FROM: {orbitFrom}")
# print(f"MAP_TO  : {orbitTo}")
# print(f"DIST: {orbitDist}")
# print(f"TOTAL: {totalDist}")
