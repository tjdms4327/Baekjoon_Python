# bronzeI_1145
import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))
nums.sort()

n = nums[0]
while True:
    possible_divide = sum(1 for x in nums if n%x == 0)
    
    if possible_divide >= 3:
        print(n)
        exit()
    n += 1