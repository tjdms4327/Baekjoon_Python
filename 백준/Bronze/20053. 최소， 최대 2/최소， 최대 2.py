import sys
input=sys.stdin.readline
    
t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    nums=list(map(int, input().strip().split()))
    print(min(nums), max(nums))