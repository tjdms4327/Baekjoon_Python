# goldIII_1414
import sys
input = sys.stdin.readline
from queue import PriorityQueue

n = int(input()) # 컴퓨터 수
pq = PriorityQueue() # 랜선 정보 저장
sum = 0 # 모든 랜선의 합 저장 변수
for i in range(n):
    tempc = list(input())
    for j in range(n):
        if 'a' <= tempc[j] <= 'z':
            temp = ord(tempc[j]) - ord('a') + 1
        elif 'A' <= tempc[j] <= 'Z':
            temp = ord(tempc[j]) - ord('A') + 27
        else:
            temp = 0
        sum += temp # 총 랜선의 길이 저장
        if i != j and temp != 0:
            pq.put((temp, i, j)) # 랜선 길이 우선 정렬
        
parent = [0] * n
for i in range(n):
    parent[i] = i

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
    
useEdge = 0
result = 0
while pq.qsize() > 0: # 최소 신장 트리 알고리즘
    v, s, e = pq.get()
    if find(s) != find(e):
        union(s, e)
        result += v
        useEdge += 1
        
if useEdge == n-1:
    print(sum - result)
else:
    print(-1)