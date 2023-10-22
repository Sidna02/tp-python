source = [1, 2, 5, 8, 6, 2, 5, 9, 1, 8, 8]

d = {}

for i, j in enumerate(source):
    c = source.count(j)
    if c > 1 and j not in d:
        d[j] = c
print(d)

for key in d:
    for x in range(d[key] - 1):
        source.remove(key)

print(source)
