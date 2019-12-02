
fp = open("input_2.txt", "r")
lines = fp.readlines()

accum = 0
for line in lines:
    mass = int(line.strip())

    subAccum = 0
    val = int(mass / 3) - 2
    while val > 0:
        subAccum += val
        val = int(val / 3) - 2

    accum += subAccum
    print(f"mass={mass}, subAccum={subAccum}, accum={accum}")
