t=int(input())
for i in range(1, t+1):
    val=0
    n,s,d=map(int,input().split())
    for _ in range(n):
        di,vi=map(int,input().split())
        if di<=d*s:
            val+=vi
    print(f'Data Set {i}:\n{val}')
    print()