#            A B C D E F
# startVal = 2 5 4 0 3 2
# endVal =   7 8 9 8 6 0

accum = 0
count = 0
for a in range(2, 8):
    for b in range(5, 9):
        for c in range(4, 10):
            for d in range(0, 9):
                for e in range(3, 7):
                    for f in range(2, 10):
                        hasSeq = a <= b and b <= c and c <= d and d <= e and e <= f
                        hasDouble = a == b or b == c or c == d or d == e or e == f
                        accum += 1

                        # print(f"{a}{b}{c}{d}{e}{f}: hasSeq={hasSeq}, hasDouble={hasDouble}, count={count}")

                        if(hasSeq and hasDouble):
                            count += 1
                            print(f"{a}{b}{c}{d}{e}{f}; count={count}")

                        # if(accum > 30): exit()


# for a in range(2, 8):
#     aIsStart = a == 2
#     aIsEnd = a == 7
#     bStart = 5 if aIsStart else max(a, 5)
#     bEnd = (8 if aIsEnd else 9)

#     for b in range(bStart, bEnd + 1):
#         bIsStart = a == 2 and b == 5
#         bIsEnd = a == 7 and b == 9
#         cStart = 4 if bIsStart else max(b, 4)
#         cEnd = 9 if bIsEnd else 9

#         for c in range(cStart, cEnd + 1):
#             cIsStart = a == 2 and b == 5 and c == 4
#             cIsEnd = a == 7 and b == 9 and c == 9
#             dStart = 0 if cIsStart else max(c, 0)
#             dEnd = 8 if cIsEnd else 9

#             for d in range(dStart, dEnd + 1):
#                 dIsStart = a == 2 and b == 5 and c == 4 and d == 0
#                 dIsEnd = a == 7 and b == 9 and c == 9 and d == 8
#                 eStart = 3 if dIsStart else max(d, 3)
#                 eEnd = 6 if dIsEnd else 9

#                 for e in range(eStart, eEnd + 1):
#                     eIsStart = a == 2 and b == 5 and c == 4 and d == 0 and e == 3
#                     eIsEnd = a == 7 and b == 9 and c == 9 and d == 8 and e == 6
#                     fStart = 2 if eIsStart else max(e, 2)
#                     fEnd = 0 if eIsEnd else 9

#                     for f in range(fStart, fEnd + 1):
#                         print(f"{a}{b}{c}{d}{e}{f}")

#                         if(a == b or b == c or c == d or d == e or e == f):
#                             count += 1
#                             # print(f"{a}{b}{c}{d}{e}{f}; count={count}")

#                         if(count > 10): exit()


print(f"count={count}")
