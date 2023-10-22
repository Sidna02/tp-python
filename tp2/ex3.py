import random

n = random.randint(1, 100)
print("Choissir un nombre entre 1 et 100, vous avez 7 essais")

trouve = False
tries = 0
print(n)
while not trouve and tries < 7:
    tries += 1
    a = int(input("donner un nombre"))
    if a != n:
        print("ops")
    else:
        print("Vous avez le devine en ", tries)
        trouve = True
if tries == 7:
    print("J'ai gagné le nombre est ", n)