import sys
input = sys.stdin.readline
from collections import Counter

nums = list(map(int, input().strip()))

standard = set([2, 0, 1, 8])

if set(nums).issubset(standard):
    if set(nums) == standard:
        count = Counter(nums)        
        if len(set(count.values())) == 1:
            print(8)
        else:
            print(2)
    else:
        print(1)
else:
    print(0)