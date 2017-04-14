a=float(input("введите длину стороны a "))
b=float(input("введите длину стороны b "))
c=float(input("введите длину стороны c "))
if (a+b>c) and (a+c>b) and (b+c>a) and (a>0) and (b>0) and (c>0):
    print("такой треугольник существует")
else:
    print("такой треугольник не существует")
