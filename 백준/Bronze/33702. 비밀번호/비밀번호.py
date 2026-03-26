import sys
input = sys.stdin.readline

k = int(input())

pos = {1:(0,0), 2:(0,1), 3:(0,2),
       4:(1,0), 5:(1,1), 6:(1,2),
       7:(2,0), 8:(2,1), 9:(2,2)}

d = [(-1,0), (1,0), (0,-1), (0,1)]

def dfs(cur, visited):
    if len(visited)==9:
        return 1
    
    count = 0
    x, y = pos[cur]
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        
        if 0<=nx<3 and 0<=ny<3:
            next_btn = nx*3+ny+1
            if next_btn not in visited:
                visited.add(next_btn)
                count += dfs(next_btn, visited)
                visited.remove(next_btn)
    return count

visited = set([k])
print(dfs(k, visited))