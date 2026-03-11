import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
roads = [list(input().strip()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0

def dfs(row, col, distance):
    global cnt
    
    if row==0 and col==c-1:
        if distance == k:
            cnt += 1
        return
    
    for i in range(4):
        x, y = row+dx[i], col+dy[i]
        if 0<=x<r and 0<=y<c and roads[x][y] == '.':
            roads[x][y] = 'T'
            dfs(x, y, distance+1)
            roads[x][y] = '.'

roads[r-1][0] = 'T'           
dfs(r-1, 0, 1)
print(cnt)