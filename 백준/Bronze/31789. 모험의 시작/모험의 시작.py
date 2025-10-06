# bronzeIII_31789
import sys
input = sys.stdin.readline

n = int(input())
x, s = map(int, input().split())
for _ in range(n):
    c, p = map(int, input().split())
    if c <= x and p > s:
        print('YES')
        sys.stdin.read()
        exit()
    else:
        continue
print('NO')