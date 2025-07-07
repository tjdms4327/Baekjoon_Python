n=int(input())

for i in range(1,n*5+1):
    if i<=n or 2*n<i<=3*n:
        print('@'*n*5)
    else:
        print('@'*n)