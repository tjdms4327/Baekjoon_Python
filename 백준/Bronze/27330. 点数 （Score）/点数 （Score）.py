import sys
input=sys.stdin.readline

n=int(input().strip())
A=list(map(int, input().strip().split()))
m=int(input().strip())
B=list(map(int, input().strip().split()))

result=0
for i in A:
    result+=i
    if result in B:
        result=0
print(result)