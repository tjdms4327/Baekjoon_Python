import sys
input=sys.stdin.readline

n=int(input())
matrix=[list(map(int, input().split())) for _ in range(n)]



visited=[[False]*n for _ in range(n)]
found=False

def dfs(x, y):
    global found
    
    if x<0 or x>=n or y<0 or y>=n:
        return 
    if visited[x][y]:
        return
    if matrix[x][y]==-1:
        found=True
        return 

    visited[x][y]=True
    jump=matrix[x][y]
    dfs(x+jump, y) # 아래로 이동
    dfs(x, y+jump) # 오른쪽으로 이동

dfs(0,0)
print("HaruHaru" if found else "Hing")
