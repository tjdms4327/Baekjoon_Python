a=list(map(int,input().split()))
while sum(a) !=0:
    a.sort()
    x=a[0]**2+a[1]**2 ; y=a[-1]**2
    if x==y:
        print('right')
    else:
        print('wrong')
    a=list(map(int,input().split()))