import random
a=b=5 #размеры
mas=[]
for i in range(a):
    mas.append([])
    for j in range(b):
        g=-1*random.randint(-10,10)*3
        mas[i].append(g)
print(mas)
