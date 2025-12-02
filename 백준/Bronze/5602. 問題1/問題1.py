import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split()))for _ in range(n)]

like = []
for idx, col in enumerate(zip(*matrix)):
    count = col.count(1)
    like.append((count, idx+1))
like.sort(key = lambda x:(-x[0], x[1]))

for x in like:
    print(x[1], end=' ')