# bronzeIII_32500
import sys
input = sys.stdin.readline

n = int(input())
num = [0]*51
for _ in range(10*n):
    X = list(map(int, input().split()))
    for x in X:
        num[x] += 1
        
result = [idx for idx, x in enumerate(num) if x > 2*n]
if result:
    print(*result)
else:
    print(-1)