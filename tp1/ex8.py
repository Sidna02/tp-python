print(range(0, 4))
notes = 0
moyenne = 0
note = 0
sommeCoef = 0
for i in range(1, 5):
    note = float(input("Donner la " + str(i) + " note"))
    coef = int(input("Donner la coef"))
    sommeCoef += coef
    notes += note * coef

notes /= sommeCoef
print(notes)

if notes >= 10:
    print("Validé")
elif 7 <= notes < 10:
    print("Rattrapage")
else:
    print("NV")
