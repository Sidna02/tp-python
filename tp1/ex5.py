n = int(input("Donner un nombre"))
if n % 2 == 0:
    print("pair")
elif n % 2 != 0 and n % 3 == 0:
    print("impair et multiple de 3")
else:
    print("ni pair ni mult de 3")
