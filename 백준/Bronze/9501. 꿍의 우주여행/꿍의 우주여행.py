t=int(input())

for _ in range(t):
    n,d=map(int, input().split())
    possible=0
    for _ in range(n):
        v,f,c=map(float, input().split())
        if (f/c)*v>=d:
            possible+=1
    print(possible)