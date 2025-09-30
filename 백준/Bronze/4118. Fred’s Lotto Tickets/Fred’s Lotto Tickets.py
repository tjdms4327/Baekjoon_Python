# bronzeIII_4118
import sys
input = sys.stdin.readline

while True:  
    n = int(input())
    if n == 0: break
    
    nums = []
    for _ in range(n):
        nums.extend(list(map(int, input().split())))
    if len(set(nums)) == 49:
        print('Yes')
    else:
        print('No')