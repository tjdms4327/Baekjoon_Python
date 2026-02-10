import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    X = list(map(int, input().split()))
    
    reversed_nums = []
    X[-1] += X[5]
    X[5] = 0
    for idx, x in enumerate(X, start=1):
        if x != 0:
            reversed_nums.extend([str(idx)]*x)
    
    nums = reversed_nums[::-1]
    length = len(reversed_nums)
    
    l, reversed_r = [], []
    for i in range(length):
        if i % 2 == 0:
            l.append(nums[i])
        else:
            reversed_r.append(nums[i])
            
    print(' '.join(l+reversed_r[::-1]))