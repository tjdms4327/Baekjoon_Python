# goldV_1717.py
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
parent = [0] * (n+1)

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a]) # 재귀 압축
        return parent[a]
    
def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        
def checkSame(a, b): # 두 원소가 같은 집합에 속해있는지 확인
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False

for i in range(0, n+1):
    parent[i] = i

for i in range(m):
    q, a, b = map(int, input().split())
    if q == 0:
        union(a, b)
    else:
        if checkSame(a, b):
            print('YES')
        else:
            print('NO')