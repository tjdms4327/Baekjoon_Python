# goldIII_1516
from collections import deque

n = int(input())
A = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
selfBuild = [0] * (n+1)

for i in range(1, n+1):
    inputList = list(map(int, input().split()))
    selfBuild[i] = (inputList[0])
    index = 1
    while True:  
        preTemp = inputList[index]
        index += 1
        if preTemp == -1:
            break
        A[preTemp].append(i)
        indegree[i] += 1 # 진입차수 데이터 저장

queue = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)

result = [0] * (n+1)

while queue: # 위상 정렬 수행
    now = queue.popleft()
    for next in A[now]:
        indegree[next] -= 1
        result[next] = max(result[next], result[now]+selfBuild[now])
        if indegree[next] == 0:
            queue.append(next)

for i in range(1, n+1):
    print(result[i] + selfBuild[i])