# bronzeIII_9298
import sys
input = sys.stdin.readline

t = int(input())
for case in range(1, t+1):
    n = int(input())
    
    X, Y = [], []
    for _ in range(n):
        x, y = map(float, input().split())
        X.append(x)
        Y.append(y)
    
    X.sort() ; Y.sort()
    side_x = X[-1] - X[0]
    side_y = Y[-1] - Y[0]
    print(f'Case {case}: Area {side_x * side_y}, Perimeter {(side_x + side_y) * 2}')