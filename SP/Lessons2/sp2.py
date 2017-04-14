n=int(input("введите n "))
m=int(input("введите m "))
k=int(input("введите k "))
l=int(input("введите l "))
if n>k:
    if m>l:
        buf=m
        m=l
        l=buf
if (n+m)>k:
    print("true")
else:
    print("false")
