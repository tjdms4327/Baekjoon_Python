t=int(input())
for i in range(t):
    a=input().split()
    b=float(a[0])
    for j in range(1,len(a)):
        if a[j]=='@':
            b=b*3
        elif a[j]== '%':
            b+=5
        else:
            b-=7
    print('{:.2f}'.format(b))