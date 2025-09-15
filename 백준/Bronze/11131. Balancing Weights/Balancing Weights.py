import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    w = list(map(int, input().split()))
    
    if sum(w) < 0:
        print('Left')
    elif sum(w) == 0:
        print('Equilibrium')
    else:
        print('Right')