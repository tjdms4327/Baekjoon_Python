import sys
input=sys.stdin.readline

n=int(input())
next_person=[0]+[int(input()) for _ in range(n)] # 1-indexed



def dfs(start):
    visited=[False]*(n+1)
    cnt=0
    cur=start
    while not visited[cur]:
        visited[cur]=True
        cnt+=1
        cur=next_person[cur]
    return cnt

max_cnt, answer=0,0
for i in range(1, n+1):
    count=dfs(i)
    if count>max_cnt:
        max_cnt=count
        answer=i
print(answer)