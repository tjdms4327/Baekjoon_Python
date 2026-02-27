import sys
input = sys.stdin.readline

n = int(input())
P = [tuple(map(int, input().split())) for _ in range(n)]

t = int(input())
for _ in range(t):
    i, dv = map(int, input().split())
    i -= 1
    
    x, y = P[i]
    
    count = 0
    for j in range(n):
        nx, ny = P[j]
        if i!=j and (nx-x)**2+(ny-y)**2 <= dv**2:
            count += 1
    
    print(count)