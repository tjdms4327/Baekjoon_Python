import sys
input = sys.stdin.readline

golden = (1 + 5**0.5) / 2

n = int(input())
for _ in range(n):
    nums = list(map(float, input().split()))
    a, b = max(nums), min(nums)
    
    if golden*0.99 <= a/b <= golden*1.01:
        print('golden')
    else:
        print('not')