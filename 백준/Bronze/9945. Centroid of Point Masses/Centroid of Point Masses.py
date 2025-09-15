import sys
input = sys.stdin.readline

case = 0
while True:
    n = int(input())
    if n < 0: break
    
    case += 1
    Mx, My = 0, 0
    M = 0
    for i in range(n):
        xi, yi, mi = map(int, input().split())
        Mx += mi*xi
        My += mi*yi
        M += mi
        
    print(f'Case {case}: {Mx/M:.2f} {My/M:.2f}')
    input()