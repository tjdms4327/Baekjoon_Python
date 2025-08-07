import sys
input=sys.stdin.readline

n, k=map(int, input().split())
A=[int(input()) for _ in range(n)]



visited=[False]*n
count=1
cur=0
visited[cur]=True

while True:
    cur=A[cur]
    count+=1
    if cur==k:
        print(count-1)
        break
    if visited[cur]:
        print(-1)
        break
    visited[cur]=True
    