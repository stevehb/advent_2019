
droidMap = []

fp = open("map_data.txt", "r")
lines = fp.readlines()
for line in lines:
    line = line.strip()
    if not line: break
    droidMap.append(list(line))

oxyX = -1
oxyY = -1
MAX_X = len(droidMap[0])
MAX_Y = len(droidMap)
for y in range(MAX_Y):
    for x in range(MAX_X):
        if(droidMap[y][x] == 'O'):
            oxyX = x
            oxyY = y

print(f"Map dims: [{MAX_X}, {MAX_Y}]")
print(f"Oxygen at: [{oxyX}, {oxyY}] ")

counter = 0
maxGen = -1
queue = [(oxyX, oxyY, 0)]
while queue:
    counter += 1
    pos = queue.pop(0)
    x = pos[0]
    y = pos[1]
    gen = pos[2]
    if(gen > maxGen): maxGen = gen
    # NORTH
    if(droidMap[y-1][x] == " "):
        droidMap[y-1][x] = "O"
        queue.append((x, y-1, gen+1))
    # SOUTH
    if(droidMap[y+1][x] == " "):
        droidMap[y+1][x] = "O"
        queue.append((x, y+1, gen+1))
    # EAST
    if(droidMap[y][x+1] == " "):
        droidMap[y][x+1] = "O"
        queue.append((x+1, y, gen+1))
    # WEST
    if(droidMap[y][x-1] == " "):
        droidMap[y][x-1] = "O"
        queue.append((x-1, y, gen+1))            

print(f"Total iter: {counter}")
print(f"Max generation: {maxGen}")
