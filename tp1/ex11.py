poids = int(input("Donner le poids"))
taille = float(input("Donner la taille"))
res = poids / taille
print(res)
if res > 40:
    print("Obesité morbide ou massive")
elif 40 >= res >= 35:
    print("obésité servere")
elif 35 >= res >= 30:
    print("obésité modere")
elif 30 >= res >= 25:
    print("Surpoids")
elif 25 >= res >= 18.5:
    print("corpulence normale")
elif 18.5 >= res >= 16.5:
    print("maigreur")
else:
    print("Famine")
