import sys
input=sys.stdin.readline

n,k=map(int, input().strip().split())
temp=list(map(int, input().strip().split()))
S=[0]*(n+1)
for i in range(n):
    S[i+1]=S[i]+temp[i]

cand=[]
for i in range(n-k+1):
    cand.append(S[i+k]-S[i])
#print(cand)
print(max(cand))