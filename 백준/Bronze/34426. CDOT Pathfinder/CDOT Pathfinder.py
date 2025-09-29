# bronzeIII_34426
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    leg = int(input())
    nums = list(map(int, input().split()))
    
    time = [0] * leg
    for i in range(leg):
        time[i] = nums[2*i+1] / nums[2*i]
    print(time.index(min(time)) + 1)