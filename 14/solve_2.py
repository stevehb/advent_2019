import math


# for pnt in [(0.1, 1), (1, 1), (1, 0.1), (1, -0.1), (1, -1), (0.1, -1), (-0.1, -1), (-1, -1), (-1, -0.1), (-1, 0.1), (-1, 1), (-0.1, 1)]:
#     rad = math.atan2(pnt[0], pnt[1])
#     if(rad < 0):
#         rad = (math.pi + rad) + math.pi
#     print(f"[{pnt[0]:.2f}, {pnt[1]:.2f}]:\t\tangle={rad:.2f}")

# exit()



def gatherAsteroids(map, x0, y0):
    xMax = len(map[0])
    yMax = len(map)
    asteroidVectors = {}
    for y1 in range(0, yMax):
        for x1 in range(0, xMax):
            if(x0 == x1 and y0 == y1):
                continue
            if(map[y1][x1] != '#'):
                continue
            xDist = x1 - x0
            yDist = y1 - y0
            divisor = max(abs(xDist), abs(yDist))
            radians = math.atan2(xDist / divisor, yDist / divisor)
            if(radians < 0):
                radians = (math.pi + radians) + math.pi
            if(radians not in asteroidVectors):
                asteroidVectors[radians] = []
            dist = math.sqrt(xDist**2 + yDist**2)
            asteroidVectors[radians].append((dist, x1, y1))
    return asteroidVectors

fp = open("input.txt", "r")
lines = fp.readlines()
map = []
for line in lines:
    line = line.strip()
    if(len(line) == 0): break
    row = list(line)
    map.append(row)

xMax = len(map[0])
yMax = len(map)
print(f"Map size: [{xMax}, {yMax}]")

maxLinesOfSight = 0
bestPos = (-1, -1)
bestVectorMap = {}
for y in range(0, yMax):
    for x in range(0, xMax):
        if(map[y][x] != '#'): 
            continue
        vectorMap = gatherAsteroids(map, x, y)
        if(len(vectorMap) > maxLinesOfSight):
            maxLinesOfSight = len(vectorMap)
            bestVectorMap = vectorMap
            bestPos = (x, y)
    print(f"    Finished row {y}")

print(f"Best pos: {bestPos}")
print(f"Max lines of sight: {maxLinesOfSight}")

sortedKeys = sorted(bestVectorMap)
sortedMap = {}
for dirKey in sortedKeys:
    sortedMap[dirKey] = sorted(bestVectorMap[dirKey], key=lambda x: x[0])
    # print(f"DIR: {dirKey}: len={len(sortedMap[dirKey])}: {sortedMap[dirKey]}")

counter = 0
hasMore = True
while(hasMore):
    hasMore = False
    for dirKey, asteroids in sortedMap.items():
        if(len(asteroids) == 0): continue
        asteroid = asteroids.pop(0)
        counter += 1
        print(f"Asteroid[{counter}]: [{asteroid[1]}, {asteroid[2]}] at dir={dirKey}, dist={asteroid[0]}")
        hasMore = hasMore or len(asteroids) > 0

