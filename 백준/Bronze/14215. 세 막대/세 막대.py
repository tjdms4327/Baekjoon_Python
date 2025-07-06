a=sorted(list(map(int,input().split())))
if a[2]<a[0]+a[1]:
    print(sum(a))
else:
    print((a[0]+a[1])*2-1)