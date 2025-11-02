# bronzeII_32400
import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))

idx20 = nums.index(20)
if idx20 == 0:
    alice = (nums[0] + nums[1] + nums[-1]) / 3
elif idx20 == 19:
    alice = (nums[-2] + nums[-1] + nums[0]) / 3
else:
    alice = (nums[idx20-1] + nums[idx20] + nums[idx20+1]) / 3
bob = sum(nums) / 20

if alice < bob:
    print('Bob')
elif alice == bob:
    print('Tie')
else:
    print('Alice')