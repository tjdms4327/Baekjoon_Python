n=int(input())
for i in range(1,n+1):
    if i==1:
        print(' '*(n-i)+'*')
    elif i<n:
        print(' '*(n-i)+'*'+' '*(2*i-3)+'*')
    else:
        print('*'*(2*n-1))