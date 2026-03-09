import sys
input = sys.stdin.readline

n = int(input())

def dfs(remain, max_val, path):
    if remain == 0:
        print(*path)
        return
    
    for i in range(min(max_val, remain), 0, -1):
        dfs(remain-i, i, path+[i])

dfs(n, n,[])