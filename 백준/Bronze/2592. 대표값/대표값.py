# bronzeII_2592
import sys
input = sys.stdin.readline
from collections import Counter

nums = [int(input()) for _ in range(10)]

print(int(sum(nums)/10))

nums_count = Counter(nums).most_common()
print(nums_count[0][0])