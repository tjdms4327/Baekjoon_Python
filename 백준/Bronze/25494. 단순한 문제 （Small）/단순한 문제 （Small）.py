import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    nums=list(map(int, input().split()))
    print(min(nums))