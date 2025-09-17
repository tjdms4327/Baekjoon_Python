import sys
input = sys.stdin.readline

w = int(input()) # 케이크 너비
n = int(input()) # 조각 수 

area = 0
for _ in range(n):
    wi, li = map(int, input().split())
    area += (wi * li)
print(area//w)