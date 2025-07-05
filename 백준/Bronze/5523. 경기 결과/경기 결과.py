import sys
input=sys.stdin.readline

n=int(input())
A,B=0,0
for _ in range(n):
    a,b=map(int, input().split())
    if a>b:
        A+=1
    elif a<b:
        B+=1
print(A, B)