import sys
input = sys.stdin.readline

case = 0
while True:
    n = int(input())
    if n == 0:
        break
    
    case += 1
    names = [input().strip() for _ in range(n)]
    
    earings = []
    for _ in range(2*n-1):
        idx, x = input().strip().split()
        earings.append(idx)
    for i in range(1, n+1):
        if earings.count(str(i)) != 2:
            print(case, names[i-1])
            break