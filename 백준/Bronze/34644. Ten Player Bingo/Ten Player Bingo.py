import sys
input = sys.stdin.readline

nums = list(input().strip().split())

x = nums[-1]
if int(x)%10==0:
    print(10)
else:
    print(x[-1])