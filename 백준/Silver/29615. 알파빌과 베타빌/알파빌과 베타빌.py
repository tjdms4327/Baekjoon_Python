import sys
input = sys.stdin.readline

n, m = map(int, input().split())
wrote = list(map(int, input().split()))
min = set(map(int, input().split()))

cnt = 0
for x in wrote[:m]:
    if x not in min:
        cnt += 1
        
print(cnt)