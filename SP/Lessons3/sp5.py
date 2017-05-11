n=int(input("введите число "))
def avto(i):
    b=1
    a=i
    while a>=10: #узнаю сколько знаков в числе
        b=b+1
        a=a//10
    b=10**b
    if i==(i**2)%b:
        print(i**2,i)
g=1
while g<=n:
    avto(g)
    g=g+1

