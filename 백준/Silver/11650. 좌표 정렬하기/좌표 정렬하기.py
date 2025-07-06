n=int(input())

xy=[]
for i in range(n):
    xy.append(list(map(int, input().split())))
xy.sort()

for i in xy:
    print(*i, end=' ')
    print()