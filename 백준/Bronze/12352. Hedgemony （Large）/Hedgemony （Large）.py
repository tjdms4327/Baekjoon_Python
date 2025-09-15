import sys
input =sys.stdin.readline
print = sys.stdout.write

t = int(input())
for case in range(1, t+1):
    n = int(input())
    nums = list(map(int, input().split()))
    
    tmp = [0] * n
    tmp[0] = nums[0]
    for i in range(1, n-1):
        avg = (tmp[i-1] + nums[i+1]) / 2
        if nums[i] <= avg:
            tmp[i] = nums[i]
        else:
            tmp[i] = avg
    print(f'Case #{case}: {tmp[-2]:.6f}\n')