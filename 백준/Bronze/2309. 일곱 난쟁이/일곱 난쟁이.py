from itertools import combinations
dwarves = []
for _ in range(0,9):
    dwarves.append(int(input()))
dwarves.sort()
for i in combinations(dwarves, 7):
    if sum(i) == 100:
        for j in i:
            print(j)
        break