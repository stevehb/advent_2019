import itertools
import time

nLoops = 101741582076661
nLoops = 10
nCards = 119315717514047
cardVal = 2020
cardIdx = 2020

loopCnt = 0
print(f"[{loopCnt:2d}] cardIdx={cardIdx}")
positions = set()
positions.add(cardIdx)

t0 = time.perf_counter()
for _ in itertools.repeat(None, nLoops):
    startIdx = cardIdx
    cardIdx = (cardIdx * 31) % nCards
    cardIdx = nCards - (cardIdx + 1)
    cardIdx = nCards - (119315717506489 - cardIdx)
    cardIdx = (cardIdx * 49) % nCards
    cardIdx -= 194
    cardIdx = (cardIdx * 23) % nCards
    cardIdx = nCards - (119315717509156 - cardIdx)
    cardIdx = (cardIdx * 53) % nCards
    cardIdx = nCards - (5938 - cardIdx)
    cardIdx = (cardIdx * 61) % nCards
    cardIdx = nCards - (7454 - cardIdx)
    cardIdx = nCards - (cardIdx + 1)
    cardIdx = (cardIdx * 31) % nCards
    cardIdx = nCards - (3138 - cardIdx)
    cardIdx = (cardIdx * 53) % nCards
    cardIdx = nCards - (3553 - cardIdx)
    cardIdx = (cardIdx * 61) % nCards
    cardIdx = nCards - (119315717508223 - cardIdx)
    cardIdx = (cardIdx * 42) % nCards
    cardIdx = nCards - (119315717513158 - cardIdx)
    cardIdx = (cardIdx * 34) % nCards
    cardIdx = nCards - (7128 - cardIdx)
    cardIdx = (cardIdx * 42) % nCards
    cardIdx = nCards - (119315717505044 - cardIdx)
    cardIdx = (cardIdx * 75) % nCards
    cardIdx -= 13
    cardIdx = (cardIdx * 75) % nCards
    cardIdx = nCards - (119315717510982 - cardIdx)
    cardIdx = (cardIdx * 74) % nCards
    cardIdx = nCards - (119315717505891 - cardIdx)
    cardIdx = (cardIdx * 39) % nCards
    cardIdx = nCards - (4242 - cardIdx)
    cardIdx = (cardIdx * 24) % nCards
    cardIdx = nCards - (119315717513642 - cardIdx)
    cardIdx = (cardIdx * 27) % nCards
    cardIdx = nCards - (6273 - cardIdx)
    cardIdx = (cardIdx * 19) % nCards
    cardIdx = nCards - (119315717504221 - cardIdx)
    cardIdx = (cardIdx * 58) % nCards
    cardIdx = nCards - (cardIdx + 1)
    cardIdx = nCards - (119315717507120 - cardIdx)
    cardIdx = (cardIdx * 65) % nCards
    cardIdx = nCards - (119315717504141 - cardIdx)
    cardIdx = (cardIdx * 31) % nCards
    cardIdx = nCards - (cardIdx + 1)
    cardIdx = (cardIdx * 42) % nCards
    cardIdx = nCards - (cardIdx + 1)
    cardIdx = (cardIdx * 39) % nCards
    cardIdx = nCards - (119315717509776 - cardIdx)
    cardIdx = nCards - (cardIdx + 1)
    cardIdx = (cardIdx * 32) % nCards
    cardIdx = nCards - (119315717505248 - cardIdx)
    cardIdx = (cardIdx * 69) % nCards
    cardIdx = nCards - (2277 - cardIdx)
    cardIdx = (cardIdx * 55) % nCards
    cardIdx = nCards - (2871 - cardIdx)
    cardIdx = (cardIdx * 54) % nCards
    cardIdx = nCards - (119315717511929 - cardIdx)
    cardIdx = (cardIdx * 15) % nCards
    cardIdx -= 1529
    cardIdx = (cardIdx * 57) % nCards
    cardIdx = nCards - (119315717509302 - cardIdx)
    cardIdx = (cardIdx * 23) % nCards
    cardIdx = nCards - (119315717508088 - cardIdx)
    cardIdx = (cardIdx * 58) % nCards
    cardIdx = nCards - (cardIdx + 1)
    cardIdx = (cardIdx * 48) % nCards
    cardIdx = nCards - (cardIdx + 1)
    cardIdx = nCards - (2501 - cardIdx)
    cardIdx = nCards - (cardIdx + 1)
    cardIdx = (cardIdx * 42) % nCards
    cardIdx = nCards - (cardIdx + 1)
    cardIdx -= 831
    cardIdx = (cardIdx * 74) % nCards
    cardIdx = nCards - (119315717510928 - cardIdx)
    cardIdx = (cardIdx * 33) % nCards
    cardIdx -= 967
    cardIdx = (cardIdx * 69) % nCards
    cardIdx = nCards - (9191 - cardIdx)
    cardIdx = (cardIdx * 9) % nCards
    cardIdx = nCards - (5489 - cardIdx)
    cardIdx = (cardIdx * 62) % nCards
    cardIdx = nCards - (119315717504940 - cardIdx)
    cardIdx = (cardIdx * 14) % nCards
    cardIdx = nCards - (119315717506330 - cardIdx)
    cardIdx = (cardIdx * 56) % nCards
    cardIdx = nCards - (7900 - cardIdx)
    cardIdx = (cardIdx * 49) % nCards
    cardIdx -= 631
    cardIdx = (cardIdx * 14) % nCards
    cardIdx = nCards - (cardIdx + 1)
    cardIdx = (cardIdx * 58) % nCards
    cardIdx = nCards - (119315717504069 - cardIdx)
    cardIdx = (cardIdx * 48) % nCards
    cardIdx = nCards - (cardIdx + 1)
    cardIdx = (cardIdx * 66) % nCards
    cardIdx = nCards - (119315717512493 - cardIdx)
    cardIdx = nCards - (cardIdx + 1)
    cardIdx -= 897
    cardIdx = (cardIdx * 36) % nCards


    loopCnt += 1
    print(f"[{loopCnt:2d}] startIdx={startIdx} cardIdx={cardIdx} diff={cardIdx-startIdx}")
    if(cardIdx in positions):
        print(f" -- REPEATED INDEX!!!")
        break
    positions.add(cardIdx)

    # if loopCnt % 1000000 == 0:
    #     t1 = time.perf_counter()
    #     tDiff = t1 - t0
    #     totalTimeEst = (nLoops / loopCnt) * tDiff 
    #     print(f"    [{loopCnt}] {100 * loopCnt / nLoops}% elapsed={t1-t0:0.3f}, totalEst={totalTimeEst} sec")

print(f"\nFinal index of card {cardVal}: {cardIdx}")
