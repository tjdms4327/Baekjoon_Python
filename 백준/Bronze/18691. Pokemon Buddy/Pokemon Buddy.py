t=int(input())
for _ in range(t):
    g,c,e=map(int, input().split())
    if e<c:
        print(0)
    else:
        print((e-c)*(2*g-1))