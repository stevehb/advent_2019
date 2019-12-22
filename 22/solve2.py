import itertools
import time

# nLoops = 1
# nCards = 10007
# cardVal = 2019
# cardIdx = cardVal

nLoops = 101741582076661
nCards = 119315717514047
cardVal = 2020
cardIdx = cardVal

out = open("code_gen.py", 'w')
out.write("import itertools\n")
out.write("import time\n\n")
out.write(f"nLoops = {nLoops}\n")
out.write(f"nCards = {nCards}\n")
out.write(f"cardVal = {cardVal}\n")
out.write(f"cardIdx = {cardIdx}\n\n")

out.write("loopCnt = 0\n")
out.write("t0 = time.perf_counter()\n")
out.write("for _ in itertools.repeat(None, nLoops):\n")

fp = open("input.txt", 'r')
lines = fp.readlines()
for line in lines:
    line = line.strip()
    if not line: break

    if line.startswith("deal into"):
        out.write(f"    cardIdx = nCards - (cardIdx + 1)\n")
        
    if line.startswith("deal with"):
        incr = int(line.rsplit(' ', 1)[1])
        out.write(f"    cardIdx = (cardIdx * {incr}) % nCards\n")
    
    if line.startswith("c"):
        cutIdx = int(line.rsplit(' ', 1)[1])
        if cutIdx < 0:
            cutIdx = nCards + cutIdx
        if cardIdx < cutIdx:
            out.write(f"    cardIdx = nCards - ({cutIdx} - cardIdx)\n")
        else:
            out.write(f"    cardIdx -= {cutIdx}\n")

out.write("\n")
out.write("    loopCnt += 1\n")
out.write("    if loopCnt % 1000000 == 0:\n")
out.write("        t1 = time.perf_counter()\n")
out.write("        print(f\"    [{loopCnt}] {100 * loopCnt / nLoops}% elapsed={t1-t0:0.3f}\")\n\n")

out.write("print(f\"\\nFinal index of card {cardVal}: {cardIdx}\")\n")
out.close()

# loopCnt = 0
# t0 = time.perf_counter()
# for _ in itertools.repeat(None, nLoops):
#     for line in lineBuff:
#         if line.startswith("deal into"):
#             cardIdx = nCards - (cardIdx + 1)

#         # TODO: optimize this to just mul and mod once
#         if line.startswith("deal with"):
#             incr = int(line.rsplit(' ', 1)[1])
#             cardIdx = (cardIdx * incr) % nCards
        
#         if line.startswith("c"):
#             cutIdx = int(line.rsplit(' ', 1)[1])
#             if cutIdx < 0:
#                 cutIdx = nCards + cutIdx
#             if cardIdx < cutIdx:
#                 cardIdx = nCards - (cutIdx - cardIdx)
#             else:
#                 cardIdx -= cutIdx
#     loopCnt += 1
#     if loopCnt % 10000 == 0:
#         t1 = time.perf_counter()
#         print(f"    [{loopCnt}] {100 * loopCnt / nLoops}% elapsed={t1-t0:0.3f}")
            

# print(f"\nFinal index of card {cardVal}: {cardIdx}")
