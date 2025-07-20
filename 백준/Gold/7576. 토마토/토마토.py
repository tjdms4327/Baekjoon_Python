m, n=map(int, input().split()) # 가로 * 세로
graph=[list(map(int, input().strip().split())) for _ in range(n)]

from collections import deque
visited=[[False]*m for _ in range(n)]
# 방향 벡터 (상, 하, 좌, 우)
dx=[-1,1,0,0]
dy=[0,0,-1,1]

queue=deque()
# 익은 토마토 위치 큐에 모두 추가
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            queue.append((i, j))

# BFS
while queue:
    x, y=queue.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny]==0:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx, ny))
                
# 결과
ans=0
for row in graph:
    for val in row:
        if val==0:
            print(-1)
            exit(0)
        ans=max(ans, val)
print(ans-1) # 처음 익은 토마토가 1이니까