# goldIV_1707
from collections import deque
import sys
input = sys.stdin.readline

def BFS(start):
    global isEven
    queue = deque([start])
    check[start] = 0
    visited[start] = True
    
    while queue and isEven:
        node = queue.popleft()
        for i in A[node]:
            if not visited[i]:
                check[i] = (check[node] + 1) % 2
                visited[i] = True
                queue.append(i)
            elif check[node] == check[i]:
                isEven = False
                return

t = int(input())
for _ in range(t):
    v, e = map(int, input().split())
    A = [[] for _ in range(v+1)]
    visited = [False] * (v+1)
    check = [0] * (v+1)
    isEven = True
    
    for _ in range(e):
        a, b = map(int, input().split())
        A[a].append(b)
        A[b].append(a)
    
    for i in range(1, v+1):
        if not visited[i] and isEven:  # 방문 안 한 정점만 BFS
            BFS(i)
    
    print("YES" if isEven else "NO")