import sys
input = sys.stdin.readline

n, x, m = map(int, input().split())
boxes = [int(input()) for _ in range(m)]

cnt = [0]*(n+1)
for r in boxes:
    cnt[r] += 1

print(min(sum(cnt[1:x]), sum(cnt[x:n+1])))