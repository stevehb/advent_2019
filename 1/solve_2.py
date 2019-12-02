
fp = open("input_2.txt", "r")
line = fp.readline()
accum = 0
while line:
    line = int(line.strip())
    subAccum = 0
    val = int(line / 3) - 2
    while val > 0:
        subAccum += val
        val = int(val / 3) - 2

    accum += subAccum
    print(f"mass={line}, subAccum={subAccum}, accum={accum}")
    line = fp.readline()
