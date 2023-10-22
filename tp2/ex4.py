source = [1,-30,0,-2,500,4,2,100]
negatif = []
positif = []
for i,j in enumerate(source):
    if j >= 0:
        positif.append(j)
    else:
        negatif.append(j)

print(negatif, positif)