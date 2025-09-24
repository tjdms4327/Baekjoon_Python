# platinumV_1938
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())
A = [[] for _ in range(n+1)]
reverseA = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for i in range(m):
    s, e, v = map(int, input().split())
    A[s].append((e, v))
    reverseA[e].append((s, v))
    indegree[e] += 1

start, end = map(int, input().split())

queue = deque()
queue.append(start)
result = [0] * (n+1)

while queue: # 위상 정렬
    now = queue.popleft()
    for next in A[now]:
        indegree[next[0]] -= 1
        result[next[0]] = max(result[next[0]], result[now]+next[1])
        if indegree[next[0]] == 0:
            queue.append(next[0])

resultCount = 0
visited = [False] * (n+1)
queue.clear()
queue.append(end)
visited[end] = True

while queue: # 위상 정렬 reverse
    now = queue.popleft()
    for next in reverseA[now]:
        if result[next[0]] + next[1] == result[now]:
            resultCount += 1
            if not visited[next[0]]:
                visited[next[0]] = True
                queue.append(next[0])
print(result[end])
print(resultCount)