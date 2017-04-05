import math
c = float(input("введите емкость в Фарадах = "))
l = float(input("введите индуктивность в Генри = "))
t = 2*math.pi*math.sqrt(l*c)
v = 1/t
print("период = ",t)
print("частота = ",v)
