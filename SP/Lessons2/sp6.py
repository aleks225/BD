import math
a=int(input("Введите двухзначное число "))
x=a % 10
y=math.floor(a/10)
if (x == 3 or y == 3) and (x == 7 or y == 7):
    print("В числе есть 3 и 7")
else:
    print("3 и 7 в числе нету")

a=int(input("Введите след. двухзначное число "))
x=a % 10
y=math.floor(a/10)
if x == 9 or y == 9:
    print("В числе есть 9 ")
elif (x == 4 or y == 4) and (x == 8 or y == 8):
    print("В числе есть 4 и 8")
else:
    print("В числе нету 4 и 8 или 9")
