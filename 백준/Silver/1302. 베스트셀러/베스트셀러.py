import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
names = [input().strip() for _ in range(n)]

count = Counter(names)
max_count = max(count.values())
candidates = [name for name in count if count[name] == max_count]
print(sorted(candidates)[0])