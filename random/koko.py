from math import ceil

def koko(piles,h):
    if len(piles) == h:
        return max(piles)

    for b in range(1,h-len(piles)+1):
        count = 0
        for i in piles:
            count += ceil(i/b)
            if count > h:
                break

        if count <= h:
            return b
    
piles=[3,6,7,11]
h=8
print(koko(piles,h))