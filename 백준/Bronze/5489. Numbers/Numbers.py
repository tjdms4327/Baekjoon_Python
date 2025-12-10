import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
nums = [int(input()) for _ in range(n)]

count = Counter(nums)
max_count = max(count.values())
least_nums = [x for x, c in count.items() if c == max_count]
print(min(least_nums))