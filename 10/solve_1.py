import math
import sys

# def calcDist(Ax, Ay, Bx, By):
#     return math.sqrt((Bx-Ax)**2 + (By-Ay)**2)

# def hasInterference(map, x0, y0, x1, y1):
#     xMin = min(x0, x1)
#     xMax = max(x0, x1)
#     yMin = min(y0, y1)
#     yMax = max(y0, y1)
#     totalDist = calcDist(x0, y0, x1, y1)
#     for y in range(yMin, yMax+1):
#         for x in range(xMin, xMax+1):
#             if(x == x0 and y == y0):
#                 continue
#             if(x == x1 and y == y1):
#                 continue
#             if(map[y][x] != '#'):
#                 continue
            
#             # dxc = x - x0
#             # dyc = y - y0
#             # dxl = x1 - x
#             # dyl = y1 - y
#             # cross = dxc * dyl - dyc * dxl
#             # if(abs(cross) < 0.0001):
#             #     return True

#             firstDist = calcDist(x0, y0, x, y)
#             secondDist = calcDist(x, y, x1, y1)

#             if(firstDist + secondDist <= (totalDist + 0.000001)):
#                 return True
#     return False


def countLinesOfSight(map, x0, y0):
    xMax = len(map[0])
    yMax = len(map)
    # linesCount = 0
    dirSet = set()
    for y1 in range(0, yMax):
        for x1 in range(0, xMax):
            if(x0 == x1 and y0 == y1):
                continue
            if(map[y1][x1] != '#'):
                continue
            xDist = x1 - x0
            yDist = y1 - y0
            divisor = max(abs(xDist), abs(yDist))
            dirSet.add((xDist / divisor, yDist / divisor))
    return len(dirSet)



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
for y in range(0, yMax):
    for x in range(0, xMax):
        if(map[y][x] != '#'): 
            continue
        linesCount = countLinesOfSight(map, x, y)
        if(linesCount > maxLinesOfSight):
            maxLinesOfSight = linesCount
            bestPos = (x, y)
    print(f"    Finished row {y}")

print(f"Best pos: {bestPos}")
print(f"Max lines of sight: {maxLinesOfSight}")
