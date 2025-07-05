n=int(input())
for i in range(1,n+1):
    if i%6==0:
        print(i, end=' ')
        print('Go!', end=' ')
    else:
        print(i, end=' ')
if n%6 != 0:
    print('Go!')