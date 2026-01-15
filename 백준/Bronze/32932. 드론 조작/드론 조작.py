import sys
input = sys.stdin.readline

n, k= map(int, input().split())
obstacles = [tuple(map(int, input().split())) for _ in range(n)]

C = list(input().strip())
udrl = [(0,1), (0,-1), (1,0), (-1,0)]

x, y = 0, 0
for c in C:
    if c=='U':
        a, b = udrl[0]
    elif c=='D':
        a, b = udrl[1]
    elif c=='R':
        a, b = udrl[2]
    elif c=='L':
        a, b = udrl[3]
    
    if (x+a, y+b) not in obstacles:
        x += a
        y += b
        
print(x, y)