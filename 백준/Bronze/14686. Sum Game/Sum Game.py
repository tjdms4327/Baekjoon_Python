import sys
input=sys.stdin.readline

n=int(input().strip())
swifts=list(map(int, input().strip().split()))
team_swifts=[0]*(n+1)
for i in range(n):
    team_swifts[i+1]=team_swifts[i]+swifts[i]
semaphores=list(map(int, input().strip().split()))
team_semaphores=[0]*(n+1)
for i in range(n):
    team_semaphores[i+1]=team_semaphores[i]+semaphores[i]

cand, K=0, 0
for i in range(n+1): # 리스트의 맨 앞 값은 0이었음
    if team_swifts[i]==team_semaphores[i]:
        if team_swifts[i]>=cand:
            cand=team_swifts[i]
            K=i
            # print(cand, K)
print(K)