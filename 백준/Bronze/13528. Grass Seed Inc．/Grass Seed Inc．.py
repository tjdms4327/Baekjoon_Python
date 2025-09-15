import sys
input = sys.stdin.readline

c = float(input())
l = int(input())
ground_area = 0
for _ in range(l):
    wi, li = map(float, input().split())
    ground_area += (wi * li)
print(ground_area * c)