ttc = 0
noms = []
quantites = []
lesprix = []
for i in range(0, 2):
    nom = input("Donner le nom du " + str(i + 1) + " article")
    noms.append(nom)

    quantite = int(input("Donner la quantite du " + str(i + 1) + " article"))
    quantites.append(quantite)

    prixU = float(input("Donner le prix Unitaire du " + str(i + 1) + " article"))
    lesprix.append(prixU)
totaleFinaleHT = 0
for i in range(0, 2):
    totaleU = lesprix[i] * quantites[i]
    print("Totale pour l'article " + noms[i], totaleU)
    totaleFinaleHT += totaleU

print("TOTALE TTC ", (totaleFinaleHT * 0.2) + totaleFinaleHT)
