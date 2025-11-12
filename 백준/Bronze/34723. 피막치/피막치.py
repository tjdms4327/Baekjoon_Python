# bronzeIII_34723
import sys
input = sys.stdin.readline

P, M, C = map(int, input().split())
x = int(input())

Min = 1e9
for p in range(1, P+1):
    for m in range(1, M+1):
        for c in range(1, C+1):
            Min = min(Min, abs((p+m)*(m+c)-x))
print(Min)