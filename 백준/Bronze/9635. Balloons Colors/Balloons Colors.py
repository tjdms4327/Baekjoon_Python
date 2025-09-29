# bronzeIII_9635
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    nums = list(map(int, input().split()))
    
    if x == nums[0]:
        if y == nums[-1]:
            print('BOTH')
        else:
            print('EASY')
    elif y == nums[-1]:
        print('HARD')
    else:
        print('OKAY')