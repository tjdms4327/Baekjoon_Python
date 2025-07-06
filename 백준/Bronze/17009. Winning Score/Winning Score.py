a=0
for i in range(6):
    if i < 3:
        a+=int(input())*(3-i)
    else:
        a-=int(input())*(6-i)
if a>0:
    print('A')
elif a==0:
    print('T')
else:
    print('B')