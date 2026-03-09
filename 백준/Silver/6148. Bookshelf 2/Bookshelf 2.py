import sys
input = sys.stdin.readline

n, b = map(int, input().split())
H = [int(input()) for _ in range(n)]

ans = float('inf')
def dfs(idx, height):
    global ans
    
    if idx == n:
        if height >= b:
            ans = min(ans, height-b)
        return 
    
    dfs(idx+1, height+H[idx]) # 선택
    dfs(idx+1, height) # 선택X
    
dfs(0, 0)
print(ans)