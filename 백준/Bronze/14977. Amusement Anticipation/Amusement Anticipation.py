import sys
input = sys.stdin.readline

while True:
    line = input()
    if not line:
        break
    
    n = int(line)
    X = list(map(int, input().split()))
    
    if n <= 2:
        print(1)
        continue
    
    d = X[-1] - X[-2]
    start = n - 1
    for i in range(n-2, 0, -1):
        if X[i] - X[i-1] == d:
            start = i
        else:
            break
    print(start)