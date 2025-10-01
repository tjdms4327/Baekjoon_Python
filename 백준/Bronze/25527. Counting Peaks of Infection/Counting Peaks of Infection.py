# bronzeIII_25527
import sys
input = sys.stdin.readline

while True:  
    n = int(input())
    if n == 0: break
    
    peak, count = 0, 0
    nums = list(map(int, input().split()))
    for i in range(1, n-1):
        if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
            count += 1
    print(count)