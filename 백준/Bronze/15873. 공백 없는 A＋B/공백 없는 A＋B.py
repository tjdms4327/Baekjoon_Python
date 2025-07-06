a=input()
if len(a)<3:
    print(int(a[0])+int(a[1]))
elif len(a)==4:
    print(20)
elif a[:2]=='10':
    print(10+int(a[2]))
else:
    print(10+int(a[0]))