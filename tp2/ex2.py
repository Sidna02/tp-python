taille = int(input("Donner la taille"))
for i in range(1,taille):
    for j in range(1,i ):
        print("*", end="")
    print("\n")
for i in range(0,taille):
    for j in range(0,i ):
        print(i+1, end="")
    print("\n")