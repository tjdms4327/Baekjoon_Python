n=int(input())
for _ in range(n):
    slst=list(input().split())
    print('god', *slst[1:], sep='')