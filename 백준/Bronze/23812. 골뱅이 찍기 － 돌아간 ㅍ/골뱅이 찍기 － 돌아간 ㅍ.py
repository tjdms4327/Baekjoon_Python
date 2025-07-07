n=int(input())

for i in range(1,n*5+1):
    if n<i<=2*n or 3*n<i<=4*n:
        print('@'*n*5)
    else:
        print('@'*n+' '*3*n+'@'*n)