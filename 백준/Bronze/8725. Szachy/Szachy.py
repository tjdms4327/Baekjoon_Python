import sys
input = sys.stdin.readline

n = int(input())
total = 0
for _ in range(n):
    row = list(map(int, input().split()))
    max_num = max(row)
    if max_num > 0:
        total += max_num
print(total)