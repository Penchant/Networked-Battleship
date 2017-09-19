d = {}
with open("Btest.txt") as f:
    x = 0
    y = 0
    for line in f:
        for c in line:
            d[(x,y)] = c
            y = y + 1
        x = x + 1

print(d)
