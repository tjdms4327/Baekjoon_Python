import sys
input = sys.stdin.readline

n = int(input())
parent = [int(input()) for _ in range(n)]

root = parent.index(-1) + 1
children = [[] for _ in range(n+1)] # i번째의 자식
for node in range(1, n+1):
    p = parent[node-1]
    if p != -1:
        children[p].append(node)

height = [0 for _ in range(n+1)]
def dfs(node, h):
    height[node] = h
    
    for child in children[node]:
        dfs(child, h+1)
        
    
    
dfs(root, 0)
for x in height[1:]:
    print(x)