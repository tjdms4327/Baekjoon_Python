import sys
input = sys.stdin.readline

c,r = map(int, input().split())

X, Y = 0, 0
while True:
    x, y = map(int, input().split())
    if x==y==0:
        break
    
    if x < 0:
        X = max(0, X+x)
    elif x > 0:
        X = min(c, X+x)
    if y < 0:
        Y = max(0, Y+y)
    elif y > 0:
        Y = min(r, Y+y)
        
    print(X, Y)