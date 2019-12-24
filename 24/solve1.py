import zlib

# tiles = list("....##..#.#..##..#..#....")

# REAL INPUT:
tiles = list("##.#.##.#.##.##.####.#...")


knownTiles = {}
newTiles = tiles.copy()
loopCnt = 0

print(f"INITIAL")
for y in range(5):
    for x in range(5):
        print(tiles[5 * y + x], end="")
    print("")
print(f"")


while(True):
    loopCnt += 1

    for i in range(len(tiles)):
        newTiles[i] = tiles[i]

    for i in range(len(tiles)):
        nBug = 1 if(i > 4 and tiles[i - 5] == '#') else 0
        sBug = 1 if(i < 20 and tiles[i + 5] == '#') else 0
        eBug = 1 if(i % 5 < 4 and tiles[i + 1] == '#') else 0
        wBug = 1 if(i % 5 != 0 and tiles[i - 1] == '#') else 0
        bugSum = nBug + sBug + eBug + wBug
        if tiles[i] == '#' and bugSum != 1:
            newTiles[i] = '.'
        elif tiles[i] == '.' and (bugSum == 1 or bugSum == 2):
            newTiles[i] = '#'
        else:
            newTiles[i] = tiles[i]

    bioScore = 0
    for i in range(len(tiles)):
        tiles[i] = newTiles[i]
        if tiles[i] == '#': bioScore += 2**i

    # crc32 = zlib.crc32(b''.join(tiles))
    tileStr = ''.join(tiles)
    if tileStr in knownTiles:
        print(f"Double Known tiles at loop {loopCnt}")
        for y in range(5):
            for x in range(5):
                print(tiles[5 * y + x], end="")
            print("")
        print(f"WINNER: bioScore={bioScore}")
        exit()
    knownTiles[tileStr] = bioScore


