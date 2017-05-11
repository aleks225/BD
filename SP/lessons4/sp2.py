s=input("введите строку: ")
a=1040
s1="'"
while a<=1103:
    s1=s1+chr(a)+"'"
    a=a+1
s2="*"
for i in range(len(s1)):
    s = s.replace(s1[i], s2[0])
print(s)
    
