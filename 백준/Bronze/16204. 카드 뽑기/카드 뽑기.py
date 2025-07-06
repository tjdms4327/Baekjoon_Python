n,m,k=map(int,input().split())
 
if m==k:
    print(n)
elif m>k:
    print(k + n-m)
else:
    print(m + n-k)