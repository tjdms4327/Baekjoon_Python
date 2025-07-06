n=int(input())
for i in range(1,2*n+1):
    if n%2==0:
        if i%2==1:
            print('* '*(n//2))
        else:
            print(' *'*(n//2))
    else: 
        if i%2==1:
            print('* '*(n//2+1))
        else:
            print(' *'*(n//2))