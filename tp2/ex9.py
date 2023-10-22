while True:
    print("1. Mad vers Euro","2. Euro en Mad", "-1. Quitter")
    choix = int(input("Donner le choix"))
    if choix == -1:
        break
    elif choix == 1:
        v = float(input("Donner la valeur"))
        print(v * 0.092)
    elif choix == 2:
        v = float(input("Donner la valeur"))
        print(v * 10.86)


