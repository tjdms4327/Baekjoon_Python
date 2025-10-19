P = ['0123', '4567', '0145', '2367', '0246', '1357']

t = int(input())
for _ in range(t):
    nums = list(input().strip().split())
    nums.sort()
    
    if ''.join(nums) in P:
        print('YES')
    else:
        print('NO')