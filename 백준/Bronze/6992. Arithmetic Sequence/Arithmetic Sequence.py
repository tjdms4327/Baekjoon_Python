import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, *nums = map(int, input().split())
    
    arithmetic = True
    for i in range(n-2):
        if nums[i+2]+nums[i] != 2*nums[i+1]:
            arithmetic = False
            break
    
    if arithmetic:
        d = nums[1] - nums[0]
        result = []
        for i in range(1, 6):
            result.append(nums[-1] + d*(i))
        print(f'The next 5 numbers after [{", ".join(map(str, nums))}] are: '
              f'[{", ".join(map(str, result))}]')
    else:
        print(f'The sequence [{", ".join(map(str, nums))}] is not an arithmetic sequence.')