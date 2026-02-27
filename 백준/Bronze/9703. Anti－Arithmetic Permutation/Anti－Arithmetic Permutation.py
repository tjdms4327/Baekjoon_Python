import sys
input = sys.stdin.readline

t = int(input())
for x in range(1, 1+t):
    n = int(input())
    nums = list(map(int, input().split()))
    
    ok = True
    for j in range(n):
        for i in range(j+1, n):
            for k in range(i+1, n):
                if nums[j]+nums[k] == 2*nums[i]:
                    ok = False
                    break
        if not ok:
            break
        
    if ok:
        result = 'YES'
    else:
        result = 'NO'
        
    print(f'Case #{x}: {result}')
    