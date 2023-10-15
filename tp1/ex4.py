t = int(input("Donner les secondes"))

h = 0
m = 0
s = 0

h = int(t / 3600)
t = t % 3600
m = int(t / 60)
t = t % m
s = t

print(h, m, s)
