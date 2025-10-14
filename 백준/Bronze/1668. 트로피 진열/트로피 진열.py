# bronzeII_1668
import sys
input = sys.stdin.readline

n = int(input())
heights = [int(input()) for _ in range(n)]

left_cur, left_count = -1, 0
for h in heights:
    if left_cur < h:
        left_cur = h
        left_count += 1

right_cur, right_count = -1, 0
for h in heights[::-1]:
    if right_cur < h:
        right_cur = h
        right_count += 1

print(left_count, right_count, sep='\n')