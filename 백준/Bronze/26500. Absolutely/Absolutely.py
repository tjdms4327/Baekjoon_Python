import sys
input=sys.stdin.readline

n=int(input())
for _ in range(n):
    nums=list(map(float, input().split()))
    nums.sort()
    print(f'{nums[1]-nums[0]:.1f}')