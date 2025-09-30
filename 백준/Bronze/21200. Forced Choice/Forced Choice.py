# bronzeIII_21200
import sys
input = sys.stdin.readline

n, p, s = map(int, input().split())
for _ in range(s):
    nums = list(map(int, input().split()))
    
    if p in nums[1:]:
        print('KEEP')
    else:
        print('REMOVE')