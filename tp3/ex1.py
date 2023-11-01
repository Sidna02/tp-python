def somme(start, end):
    s = 0
    if end < start:
        end, start = start, end
    for i in range(start, end+1):
        s += i
    return s


print(somme(2, 3))