import sys, math
input = sys.stdin.readline

n, l = map(int, input().split())

pools = [tuple(map(int, input().split())) for _ in range(n)]
pools.sort()

cur = 0
cnt = 0
for s, e in pools:
    remaining = max(0, e - max(cur, s))
    need = math.ceil(remaining/l)
    cnt += need
    cur = max(cur, s) + need*l
    
print(cnt)