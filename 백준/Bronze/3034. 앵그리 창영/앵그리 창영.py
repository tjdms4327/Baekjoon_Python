n,w,h=map(int, input().split())
for _ in range(n):
    length=int(input())
    if length**2<=w**2+ h**2:
        print('DA')
    else:
        print('NE')