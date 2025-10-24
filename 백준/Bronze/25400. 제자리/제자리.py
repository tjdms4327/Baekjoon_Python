# bronzeI_25400
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

cur = 0
for a in A:
    if cur+1 == a:
        cur = a
print(n - cur)