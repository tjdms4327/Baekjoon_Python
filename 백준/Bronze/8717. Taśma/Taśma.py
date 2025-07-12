import sys
input=sys.stdin.readline

n=int(input().strip())
tapes=list(map(int, input().strip().split()))
S=[0]*(n+1)
for i in range(n):
    S[i+1]=S[i]+tapes[i]

min_cand=float('inf')
for i in range(1, n):
    cand1=S[-1]-S[i]
    cand2=S[-1]-cand1
    #print(i, cand1, cand2)
    if abs(cand1-cand2)<min_cand:
        min_cand=abs(cand1-cand2)
print(min_cand)