
fp = open("input_1.txt", "r")
lines = fp.readlines()

accum = 0
for line in lines:
    mass = int(line.strip())

    val = int(mass / 3) - 2
    accum += val
    print(f"mass={mass}, val={val}, accum={accum}")
