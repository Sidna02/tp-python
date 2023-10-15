grades = ['A', 'B', 'C', 'D', 'E']
tarifHoraire = [200, 150, 120, 100, 80]
PrimesPrixTab = [1000, 800, 500, 350, 100]
PrimesHeuresTab = [20, 20, 15, 15, 10]
grade = input("Donner grade")
heures = int(input("Donner heures"))
for i, j in enumerate(grades):
    if j == grade:
        print("salaire = ", (tarifHoraire[i] * heures) + (PrimesPrixTab[i] * (heures / PrimesHeuresTab[i])))
        break
