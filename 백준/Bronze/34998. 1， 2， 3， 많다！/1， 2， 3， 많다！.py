import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    x = int(input())
    
    equation = list(input().strip().split())
    nums = []
    for i in range(2*x+1):
        if i%2==0:
            s = equation[i]
            if s != '!':
                s = int(s)
            nums.append(s)
    
    if '!' in nums:
        print('!')
    else:
        tot = sum(nums)
        if tot > 9:
            print('!')
        else:
            print(tot)