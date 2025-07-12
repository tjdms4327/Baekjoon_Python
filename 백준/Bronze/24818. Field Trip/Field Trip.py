import sys
input=sys.stdin.readline

n=int(input().strip())
students=list(map(int, input().strip().split()))
if sum(students)%3==0: wanting=sum(students)/3
else: print(-1); sys.exit()
    
S=[0]*(n+1)
for i in range(n):
    S[i+1]=S[i]+students[i]
if (wanting in S) and (2*wanting in S):
    idx_i=S.index(wanting)
    idx_j=S.index(2*wanting)
    print(idx_i, idx_j)
else: print(-1)