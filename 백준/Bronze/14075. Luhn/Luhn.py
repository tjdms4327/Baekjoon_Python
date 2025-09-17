import sys
input = sys.stdin.readline

nums  = list(map(int, input().strip()))
count = [0] * 10
for i in range(len(nums)-2, -1, -2):
    nums[i] *= 2
    if nums[i] >= 10:
        nums[i] = nums[i] // 10 + nums[i] % 10

if sum(nums) % 10 == 0:
    print('DA')
else:
    print('NE')