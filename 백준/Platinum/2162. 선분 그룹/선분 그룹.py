# platinumV_2162
import sys
input = sys.stdin.readline

n = int(input())
parent = [-1] * (n+1)

def CCW(x1, y1, x2, y2, x3, y3):
    temp = (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)
    if temp > 0:
        return 1
    elif temp < 0:
        return -1
    return 0

def isOverlab(x1, y1, x2, y2, x3, y3, x4, y4):
    return (min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and
            min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2))

def isCross(x1, y1, x2, y2, x3, y3, x4, y4):
    if max(x1, x2) < min(x3, x4) or max(x3, x4) < min(x1, x2) \
       or max(y1, y2) < min(y3, y4) or max(y3, y4) < min(y1, y2):
        return False
    abc = CCW(x1, y1, x2, y2, x3, y3)
    abd = CCW(x1, y1, x2, y2, x4, y4)
    cda = CCW(x3, y3, x4, y4, x1, y1)
    cdb = CCW(x3, y3, x4, y4, x2, y2)
    
    if abc*abd == 0 and cda*cdb == 0:  # 일직선
        return isOverlab(x1, y1, x2, y2, x3, y3, x4, y4)
    elif abc*abd <= 0 and cda*cdb <= 0:  # 교차
        return True
    return False

def find(a):
    if parent[a] < 0:
        return a
    parent[a] = find(parent[a])
    return parent[a]
def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if parent[a] < parent[b]:
        parent[a] += parent[b]
        parent[b] = a
    else:
        parent[b] += parent[a]
        parent[a] = b

L = [[]]
for i in range(1, n+1):
    L.append(list(map(int, input().split())))
    for j in range(1, i):
        if isCross(L[i][0], L[i][1], L[i][2], L[i][3], L[j][0], L[j][1], L[j][2], L[j][3]):
            union(i, j)

ans = 0
res = 0
for i in range(1, n+1):
    if parent[i] < 0:  # 대표 노드
        ans += 1
        res = min(res, parent[i])
sys.stdout.write(f"{ans}\n{-res}\n")