import sys
input = sys.stdin.readline

n = int(input())
classes = set(input() for _ in range(n))

if len(classes) <= 4:
    print('YES')
else:
    print('NO')