import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
odd = sum(1 for i in nums if i%2==1)
even = n - odd

if (odd == even) or ((odd - even) == 1):
    print(1)
else:
    print(0)