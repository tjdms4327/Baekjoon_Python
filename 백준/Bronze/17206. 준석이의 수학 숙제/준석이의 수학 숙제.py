import sys
input = sys.stdin.readline

t = int(input())
nums = list(map(int, input().split()))

for n in nums:
    a = n//3
    b = n//7
    tot = 3*a*(a+1)//2 + 7*b*(b+1)//2
    
    c = n//21
    tot -= 21*c*(c+1)//2
    
    print(tot)