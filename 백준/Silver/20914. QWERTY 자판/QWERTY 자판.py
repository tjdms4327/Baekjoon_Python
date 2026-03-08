import sys
input = sys.stdin.readline
from collections import deque

graph = {
    'Q':['W','A'],
    'W':['Q','E','S','A'],
    'E':['W','R','D','S'],
    'R':['E','T','F','D'],
    'T':['R','Y','G','F'],
    'Y':['T','U','H','G'],
    'U':['Y','I','J','H'],
    'I':['U','O','K','J'],
    'O':['I','P','L','K'],
    'P':['O','L'],

    'A':['Q','W','S','Z'],
    'S':['W','E','A','D','Z','X'],
    'D':['E','R','S','F','X','C'],
    'F':['R','T','D','G','C','V'],
    'G':['T','Y','F','H','V','B'],
    'H':['Y','U','G','J','B','N'],
    'J':['U','I','H','K','N','M'],
    'K':['I','O','J','L','M'],
    'L':['O','P','K'],

    'Z':['A','S','X'],
    'X':['S','D','Z','C'],
    'C':['D','F','X','V'],
    'V':['F','G','C','B'],
    'B':['G','H','V','N'],
    'N':['H','J','B','M'],
    'M':['J','K','N']
}

def bfs(a, b):
    if a == b:
        return 0

    q = deque([(a,0)])
    visited = set()
    visited.add(a)

    while q:
        node, d = q.popleft()
        if node == b:
            return d
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                q.append((nxt, d+1))



t = int(input())
for _ in range(t):
    s = input().strip()
    time = len(s)  # 누르는 시간 1초

    for i in range(len(s)-1):
        time += bfs(s[i], s[i+1]) * 2 

    print(time)