import sys
input=sys.stdin.readline

n=int(input().strip())
A=list(map(int, input().strip().split()))
B=list(map(int, input().strip().split()))

cnt=0
for i in range(n):
    if A[i]!=B[i]:
        if A[i]-B[i]>0:
            cnt+=A[i]-B[i]
print(cnt)
