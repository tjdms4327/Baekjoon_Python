# bronzeIII_17588
import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

full_num = list(range(1, nums[-1]+1))
if len(full_num) == n:
    print('good job')
else:
    for i in full_num:
        if i not in nums:
            print(i)