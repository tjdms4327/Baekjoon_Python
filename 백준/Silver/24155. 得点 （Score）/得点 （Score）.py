import sys
input = sys.stdin.readline

n = int(input())
s = [int(input()) for _ in range(n)]

cnt = [0]*101
for x in s:
    cnt[x] += 1

result = [0]*102
for i in range(100, -1, -1):
    result[i] = result[i+1] + cnt[i]

for x in s:
    print(result[x+1] + 1)
