import sys
input = sys.stdin.readline

n, w, h = map(int, input().split())
for _ in range(n):
    num = int(input())
    if num**2 <= w**2 + h**2:
        print('YES')
    else:
        print('NO')