import random
a=[]
s=b=c=0
while c<17:
    b=random.randint(10,99)
    s=s+b #сумма
    a.append(b)
    c=c+1
print(a)
print(s)
