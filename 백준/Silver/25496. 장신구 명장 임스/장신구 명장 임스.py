import sys
input = sys.stdin.readline

p, n = map(int, input().split())

A = list(map(int, input().split()))
A.sort()

cnt = 0
for a in A:
    if p < 200:
        p += a
        cnt += 1
        
print(cnt)