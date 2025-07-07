n=int(input())

for i in range(1,n*5+1):
    if i<=n or i>4*n:
        print('@'*n+' '*n*3+'@'*n)
    elif n<i<=2*n or i>3*n:
        print('@'*n+' '*n*2+'@'*n)
    else:
        print('@'*n*3)