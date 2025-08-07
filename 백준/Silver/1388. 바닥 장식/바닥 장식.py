import sys
input=sys.stdin.readline

n, m=map(int, input().split())
board=[list(input().strip()) for _ in range(n)]



visited=[[False]*m for _ in range(n)]

def dfs(x, y, char):
    visited[x][y]=True
    if char=='-':
        ny=y+1
        if ny<m and not visited[x][ny] and board[x][ny]=='-':
            dfs(x, ny, char)
    elif char=='|':
        nx=x+1
        if nx<n and not visited[nx][y] and board[nx][y]=='|':
            dfs(nx, y, char)

count=0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i, j, board[i][j])
            count+=1
print(count)