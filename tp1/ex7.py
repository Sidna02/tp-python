a = int(input("Donner a"))
b = int(input("Donner b"))
op = input("Donner l'op")

if op == '-':
    print(a - b)
elif op == '+':
    print(a + b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)
else:
    print("Opération invalide")
