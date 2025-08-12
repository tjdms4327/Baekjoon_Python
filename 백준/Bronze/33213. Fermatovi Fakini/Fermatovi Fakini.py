import sys
input=sys.stdin.readline

n=int(input())
boys=list(map(int, input().strip().split()))


even=sum(x % 2 == 0 for x in boys)
odd=n-even

if even>odd: 
    marco=2
else: 
    marco=1
    
while marco in boys:
    marco+=2
print(marco)