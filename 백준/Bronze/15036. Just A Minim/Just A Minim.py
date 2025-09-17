import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

length = 0
for i in nums:
    if i == 0:
        length += 2
    else:
        length += (1/i)
print(length)