import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0: break

    nums = list(map(int, input().split()))
    if sum(nums) == 3*nums[1]: # 등차
        d = nums[1]-nums[0]
        print(n * (2 * nums[0] + (n - 1) * d) // 2)
    else: # 등비
        r = nums[1] // nums[0]
        print(nums[0] * (r ** n -1) // (r - 1))