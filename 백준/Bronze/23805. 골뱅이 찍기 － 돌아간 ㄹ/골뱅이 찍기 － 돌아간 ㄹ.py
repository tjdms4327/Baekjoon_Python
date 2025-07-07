n=int(input())

for i in range(1,n*5+1):
    if i<=n:
        print('@'*3*n+' '*n+'@'*n)
    elif i>=n*4+1:
        print('@'*n+' '*n+'@'*3*n)
    else:
        print('@'*n+' '*n+'@'*n+' '*n+'@'*n)