import math
k = int(input("введите 1 число "))
y = int(input("введите 2 число "))
a = (math.log10(k-y)+(y**4))
b = (math.exp(y)+2.335*(k**2))
print(a/b)
