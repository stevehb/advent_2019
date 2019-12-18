
fp = open("input.txt", "r")
line = fp.readline()
accum = 0
while line:
    line = line.strip()
    val = int(int(line) / 3) - 2
    accum += val
    print(f"mass={line}, val={val}, accum={accum}")
    line = fp.readline()
