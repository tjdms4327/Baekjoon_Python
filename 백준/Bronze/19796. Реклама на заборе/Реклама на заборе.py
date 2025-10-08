# bronzeIII_19796
import sys
input = sys.stdin.readline

m, n = map(int, input().split())

fence = [1] + [0] * (m)
for _ in range(n):
    l, r = map(int, input().split())
    for i in range(l, r+1):
        fence[i] = 1
        
if set(fence) == {1}:
    print('YES')
else:
    print('NO')