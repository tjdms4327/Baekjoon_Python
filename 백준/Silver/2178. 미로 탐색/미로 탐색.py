# 가중치 없는 그래프의 최단거리는 BFS로

n,m=map(int, input().split())
maze=[list(map(int, input().strip())) for _ in range(n)]
#print(maze)

from collections import deque
def bfs(x, y):
    queue=deque()
    queue.append((x, y))

    # 4방향 (상, 하, 좌, 우)
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    while queue:
        x, y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            # 범위 벗어나면 무시
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            # 0인 칸이면(벽) 무시
            if maze[nx][ny]==0:
                continue
            # 처음 방문이면 기록
            if maze[nx][ny]==1:
                maze[nx][ny]=maze[x][y]+1
                queue.append((nx, ny))
    return maze[n-1][m-1] # 도착지점 값(최단 거리)

print(bfs(0,0))