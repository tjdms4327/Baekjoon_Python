import sys
input = sys.stdin.readline
from collections import deque

target = tuple(map(int, input().split()))
start = (1,2,3,4,5,6,7,8)

def change(s, command):
    if command == 'A':
        return s[::-1]
    elif command == 'B':
        return (s[3],s[0],s[1],s[2],s[5],s[6],s[7],s[4])
    elif command == 'C':
        return (s[0],s[2],s[5],s[3],s[4],s[6],s[1],s[7])
    elif command == 'D':
        lst = list(s)
        lst[0], lst[4] = lst[4], lst[0]
        return tuple(lst)
    
queue = deque([(start, 0)])
visited = {start}

while queue:
    state, dist = queue.popleft()
    
    if state == target:
        print(dist)
        break
    
    for c in 'ABCD':
        nxt = change(state, c)
        if nxt not in visited:
            queue.append((nxt, dist+1))
            visited.add(nxt)