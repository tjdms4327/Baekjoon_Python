# bronzeI_11170
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    
    nums = [str(i) for i in range(n, m+1)]
    nums_s = ''.join(nums)
    print(nums_s.count('0'))