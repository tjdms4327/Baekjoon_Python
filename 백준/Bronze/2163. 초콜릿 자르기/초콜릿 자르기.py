n,m=map(int,input().split())
if n==1 and m==1:
    print(0)
elif n==1:
    print(m-1)
elif m==1:
    print(n-1)
else:
    print(n*m-1)