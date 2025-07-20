n=int(input())
graph=[list(map(int, input().strip())) for _ in range(n)]
visited=[[False]*n for _ in range(n)]

from collections import deque
def bfs(x, y):
    queue=deque()
    queue.append((x, y)) # 시작점
    visited[x][y]=True

    # 방향 벡터 (상, 하, 좌, 우)
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    cnt=1 # 단지 내 집 개수
    while queue:
        x, y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]==1 and not visited[nx][ny]:
                    visited[nx][ny]=True
                    queue.append((nx, ny))
                    cnt+=1
    return cnt

result=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and not visited[i][j]:
            result.append(bfs(i,j))
result.sort()
print(len(result))
print(*result, sep='\n')