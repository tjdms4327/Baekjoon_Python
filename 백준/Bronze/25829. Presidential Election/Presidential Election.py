import sys
input = sys.stdin.readline

n = int(input())

tot1, tot2 = 0,0
V1, V2 = 0, 0
for _ in range(n):
    e, v1, v2 = map(int, input().split())
    tot1 += v1
    tot2 += v2
    if v1 > v2:
        V1 += e
    elif v1 < v2:
        V2 += e

if tot1 > tot2 and V1>V2:
    print(1)
elif tot1<tot2 and V1<V2:
    print(2)
else:
    print(0)