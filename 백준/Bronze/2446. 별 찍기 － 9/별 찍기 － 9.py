n=int(input())
for i in range(1,2*n):
    if i<=n:
        print(' '*(i-1)+'*'*(2*n-2*i+1))
    else:
        print(' '*(2*n-i-1)+'*'*(2*i-2*n+1))