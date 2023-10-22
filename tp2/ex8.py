n = int(input("Donner un nombre"))
source = [4, 5, 82, 1, 1, 1, 79, 88, 44]
occ = []

y = 0

for i, j in enumerate(source):
    if source[i] == n:
        y = y + 1
        occ.append(i)

print(occ, y)
