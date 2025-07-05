t=int(input())
for _ in range(t):
    n=int(input())
    pos=list(map(int, input().split()))
    pos.sort()
    print(2*(max(pos)-min(pos)))