import math
y = int(input("введите 1 число "))
h = int(input("введите 2 число "))
a = (math.tan(y**3-h**4)+h**2)/(math.sin(h)**3+y)
print(a)
