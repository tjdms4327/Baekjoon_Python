a=0
for _ in range(10):
    t=int(input())
    if t==1:
        a+=90
    elif t==2:
        a+=180
    else:
        a-=90
#print(a)
if a%360==0:
    print('N')
elif a%360==90:
    print('E')
elif a%360==180:
    print('S')
else:
    print('W')