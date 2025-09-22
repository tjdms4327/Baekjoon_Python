# goldIV_2251.py
from collections import deque

sender = [0, 0, 1, 1, 2, 2]
receiver = [1, 2, 0, 2, 0, 1]
now = list(map(int, input().split()))
visited = [[False for j in range(201)] for i in range(201)]
answer = [False] * 201

def BFS():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    answer[now[2]] = True # 현재 C 값 체크
    while queue:
        now_node = queue.popleft()
        a, b = now_node[0], now_node[1]
        c = now[2] - a - b
        for k in range(6):
            next = [a, b, c]
            next[receiver[k]] += next[sender[k]]
            next[sender[k]] = 0
            if next[receiver[k]] > now[receiver[k]]: # 물 넘침
                next[sender[k]] = next[receiver[k]] - now[receiver[k]]
                next[receiver[k]] = now[receiver[k]]
            if not visited[next[0]][next[1]]:
                visited[next[0]][next[1]] = True
                queue.append((next[0], next[1]))
                if next[0] == 0: # A가 0일 때 C의 물 양을 정답 변수에 저장
                    answer[next[2]] = True
                    
BFS()
for i in range(len(answer)):
    if answer[i]:
        print(i, end=' ')