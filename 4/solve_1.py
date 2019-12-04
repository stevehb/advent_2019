
# startVal = 2 5 4 0 3 2
# endVal =   7 8 9 8 6 0

count = 0
accum = 0
for i in range(254032, 789860):
    a = int(i / 100000) % 10
    b = int(i / 10000) % 10
    c = int(i / 1000) % 10
    d = int(i / 100) % 10
    e = int(i / 10) % 10
    f = i % 10
    hasSeq = a <= b and b <= c and c <= d and d <= e and e <= f
    hasDouble = a == b or b == c or c == d or d == e or e == f
    accum += 1

    # print(f"{a} {b} {c} {d} {e} {f}: hasSeq={hasSeq}, hasDouble={hasDouble}, count={count}")

    if(hasSeq and hasDouble):
        count += 1
        print(f"{a}{b}{c}{d}{e}{f}; count={count}")

    # if(accum > 30): exit()

print(f"count={count}")
