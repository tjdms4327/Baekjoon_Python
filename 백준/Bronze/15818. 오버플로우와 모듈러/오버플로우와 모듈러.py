import sys
input = sys.stdin.readline

from math import prod

n, m = map(int, input().split())
A = list(map(int, input().split()))


nums = prod(A)
print(nums % m)