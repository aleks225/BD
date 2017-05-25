a = 6
b = 5
r = 0  # Чтобы было, чем заполнять
mas = []
for i in range(a):
    mas.append([])
    for j in range(b):
        mas[i].append(r)
        r += 1  # Чтобы заполнялось не одно и тоже


for j in range(b):
    r=0
    for i in range(a):
        if mas[i][j]>0:
            r=r+mas[i][j]
    print("сумма ",j," столбца=",r)

