from collections import deque
def bfs(x, y):
    queue=deque()
    queue.append((x, y)) # 시작점
    visited[x][y]=True

    while queue:
        x, y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==1 and not visited[nx][ny]:
                    visited[nx][ny]=True
                    queue.append((nx, ny))
    return 0


t=int(input())
for _ in range(t):
    m, n, k=map(int, input().split())
    graph=[[0]*m for _ in range(n)]
    for _ in range(k):
        x, y=map(int, input().split())
        graph[y][x]=1

    visited=[[False]*m for _ in range(n)]
    # 방향 벡터 (상, 하, 좌, 우)
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    result=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1 and not visited[i][j]:
                bfs(i, j)
                result+=1
    print(result)