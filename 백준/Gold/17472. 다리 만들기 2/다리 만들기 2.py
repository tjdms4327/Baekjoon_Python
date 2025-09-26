# goldI_17472
import sys
input = sys.stdin.readline
import copy
from collections import deque
from queue import PriorityQueue

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

n, m = map(int, input().split())
myMap = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    myMap[i] = list(map(int, input().split()))
visited = [[False for j in range(m)] for i in range(n)]

sNum = 1 # 섬 번호
sumlist = list([]) # 모든 섬 정보 이중 리스트
mlist = [] # 1개 섬 정보 리스트

def addNode(i, j, queue):
    myMap[i][j] = sNum
    visited[i][j] = True
    temp = [i, j]
    mlist.append(temp)
    queue.append(temp)

def BFS(i, j):
    queue = deque()
    mlist.clear()
    start = [i, j]
    queue.append(start)
    mlist.append(start)
    visited[i][j] = True
    myMap[i][j] = sNum
    while queue:
        r, c = queue.popleft()
        for d in range(4):
            tempR = dr[d]
            tempC = dc[d]
            while 0 <= r + tempR < n and 0 <= c + tempC < m:
                if not visited[r+tempR][c+tempC] and myMap[r+tempR][c+tempC] != 0:
                    addNode(r+tempR, c+tempC, queue)
                else:
                    break
                if tempR < 0:
                    tempR -= 1
                elif tempR > 0:
                    tempR += 1
                elif tempC <0:
                    tempC -= 1
                elif tempC > 0:
                    tempC += 1
    return mlist

for i in range(n):
    for j in range(m):
        if myMap[i][j] != 0 and not visited[i][j]:
            tempList = copy.deepcopy(BFS(i, j)) # deepcopy여야 주소 공유X
            sNum += 1
            sumlist.append(tempList)

pq = PriorityQueue()

for now in sumlist:
    for temp in now:
        r = temp[0]
        c = temp[1]
        now_s = myMap[r][c]
        for d in range(4):
            tempR = dr[d]
            tempC = dc[d]
            blength = 0
            while 0 <= r+tempR < n and 0 <= c+tempC <m:
                if myMap[r+tempR][c+tempC] == now_s:
                    break
                elif myMap[r+tempR][c+tempC] != 0: # 같은 섬도 아니고 바다도 아니면
                    if blength > 1: 
                        pq.put((blength, now_s, myMap[r+tempR][c+tempC]))
                    break
                else: # 바다면 다리 길이 연장
                    blength += 1
                if tempR < 0:
                    tempR -= 1
                elif tempR > 0:
                    tempR += 1
                elif tempC < 0:
                    tempC -= 1
                elif tempC > 0:
                    tempC += 1
                
def find(a):
    if  a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

parent = [0] * sNum
for i in range(len(parent)):
    parent[i] = i

useEdge = 0
result = 0
while pq.qsize() > 0:
    v, s, e = pq.get()
    if find(s) != find(e):
        union(s, e)
        result += v
        useEdge += 1

if useEdge == sNum - 2:
    print(result)
else:
    print(-1)