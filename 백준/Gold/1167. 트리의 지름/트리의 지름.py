from collections import deque

n = int(input())
A = [[] for _ in range(n+1)]
for _ in range(n):
    data = list(map(int, input().split()))
    index = 0
    s = data[index]
    index += 1
    while True:
        e = data[index]
        if e == -1:
            break
        w = data[index + 1]
        A[s].append((e, w))
        index += 2
            
def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_node = queue.popleft()
        for i in A[now_node]:
            if not visited[i[0]]:
                visited[i[0]] = True
                queue.append(i[0])
                distance[i[0]] = distance[now_node] + i[1]

distance = [0] * (n + 1)
visited = [False] * (n + 1)
BFS(1)
max = 1
for i in range(2, n+1):
    if distance[max] < distance[i]:
        max = i # 거리 리스트 값 중 max값으로 시작해 시작점 재설정
distance = [0] * (n + 1)
visited = [False] * (n + 1)
BFS(max)
distance.sort()
print(distance[-1])