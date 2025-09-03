import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))
if nums[-1] == 0:
    print(int((nums[0] + nums[1])**(1/2)))
else:
    nums.sort()
    print(nums[-2]**2 - nums[-1])