a=input()
a0=int(a)

if '7' not in a and a0%7 !=0:
    print(0)
elif '7' not in a and a0%7==0:
    print(1)
elif '7' in a and a0%7 !=0:
    print(2)
else:
    print(3)