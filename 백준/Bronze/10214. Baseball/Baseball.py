t=int(input())

for i in range(t):
    A=0 ; B=0
    for j in range(9):
        a,b=map(int,input().split())
        A+=a ; B+=b
    if A>B:
        print('Yonsei')
    elif A<B:
        print('Korea')
    else:
        print('Draw')