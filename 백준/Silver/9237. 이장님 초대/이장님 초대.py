import sys
input = sys.stdin.readline

n = int(input())
trees = list(map(int, input().split()))

trees.sort(reverse=True)

days = []
for idx, day in enumerate(trees, start=1):
    days.append(idx+day)

print(max(days)+1)