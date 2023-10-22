source = [4, 66, 777, 800, 900]
n = int(input("Donner un nombre"))
isInserted = False
for i, j in enumerate(source):
    if n <= j:
        source.insert(i, n)
        isInserted = True
        break
if not isInserted:
    source.append(n)
print(source)
