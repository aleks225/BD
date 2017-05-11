import math
n=int(input("введите N "))
x=int(input("Введите X "))
a=x
b=3
c=1
while n>1:
    if c>0:
        a=a-((x**b)/math.factorial(b))
        c=-1*c
    else:
        a=a+((x**b)/math.factorial(b))
        c=-1*c
    n=n-1
    b=b+2

print(a)    
    
