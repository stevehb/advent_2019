

cards = list(range(10007))


fp = open("input.txt", 'r')
lines = fp.readlines()
for line in lines:
    line = line.strip()
    if not line: break

    if line.startswith("deal into new stack"):
        cards.reverse()
        continue

    if line.startswith("deal with increment"):
        incr = int(line.rsplit(' ', 1)[1])
        newDeck = list([-1] * len(cards))
        newIdx = 0
        for i in range(len(cards)):
            newDeck[newIdx] = cards[i]
            newIdx += incr
            if(newIdx > len(newDeck)):
                newIdx -= len(newDeck)
        cards = newDeck
    
    if line.startswith("cut"):
        cutIdx = int(line.rsplit(' ', 1)[1])
        cards = cards[cutIdx:] + cards[:cutIdx]

print(f"\nIndex of card 2019:: {cards.index(2019)}")
