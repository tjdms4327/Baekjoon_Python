import sys
input = sys.stdin.readline

n = int(input())
s = list(input().strip().split())

idx = 0
for i in range(n):
    cur = s[i]
    length = len(cur)
    if length-1 < idx:
        print(' ', end='')
    else:
        print(cur[idx], end='')
    idx = length-1
    