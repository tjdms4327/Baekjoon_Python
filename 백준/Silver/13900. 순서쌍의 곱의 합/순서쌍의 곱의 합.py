import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
nums = list(map(int, input().split()))

ans = sum(nums)**2
for x in nums:
    ans -= x**2
print(ans//2)