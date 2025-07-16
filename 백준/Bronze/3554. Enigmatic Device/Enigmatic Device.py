n=int(input())
a=list(map(int, input().split()))
m=int(input())
for _ in range(m):
    k, l, r=map(int, input().split())
    if k==1:
        for i in range(l-1, r):
            a[i]=(a[i]**2) %2010
    elif k==2:
        print(sum(a[l-1:r]))
        