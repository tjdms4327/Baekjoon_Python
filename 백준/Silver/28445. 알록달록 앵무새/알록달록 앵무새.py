import sys
input = sys.stdin.readline

colors = list(input().strip().split()) + list(input().strip().split())
colors.sort()

for x in set(colors):
    for y in set(colors):
        print(x, y)