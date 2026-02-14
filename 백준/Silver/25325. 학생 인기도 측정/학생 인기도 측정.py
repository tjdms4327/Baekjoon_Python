import sys
input = sys.stdin.readline

n = int(input())
names = list(input().split())

liked = {name:0 for name in names}

for i in range(n):
    like = list(input().strip().split())
    for x in like:
        liked[x] += 1

popular = sorted(liked.items(), key=lambda x: (-x[1], x[0]))
for name, val in popular:
    print(name, val)