import random
a=0
b=0 
s=[]
g=0 #среднее арифм
while a<=10:
    b=random.randint(0,10) #рандомим число от 0 до 10 вкл
    s.append(b)
    g=g+b
    a=a+1
g=g/11
print(s)
print("среднее=",g)
b=0
while a>0:
    a=a-1
    if s[a]>g:
        
        b=b+1
print("элементов больше среднего",b)
