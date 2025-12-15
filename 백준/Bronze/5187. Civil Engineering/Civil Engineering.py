import sys
input = sys.stdin.readline

k = int(input())
for case in range(1, k+1):
    m, n = map(int, input().split())
    density = [0] + [int(input()) for _ in range(m)]
    
    tot = 0
    for _ in range(n):
        h, w, d, i = map(int, input().split())
        V = h*w*d
        tot += density[i] * V
    
    print(f'Data Set {case}:\n{tot}')