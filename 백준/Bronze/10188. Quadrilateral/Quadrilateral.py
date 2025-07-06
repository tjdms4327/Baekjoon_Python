n=int(input())
for _ in range(n):
    w,h=map(int,input().split())
    for _ in range(h):
        print('X'*w)
    print()