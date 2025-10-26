# bronzeII_10864
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

friends = [0 for _ in range(1, n+2)]
for _ in range(m):
    a, b = map(int, input().split())
    friends[a] += 1
    friends[b] += 1

print(*friends[1:], sep='\n')