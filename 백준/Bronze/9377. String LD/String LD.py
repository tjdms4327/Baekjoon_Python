import sys
input = sys.stdin.readline

while True:   
    n = int(input())
    if n == 0:
        break 
    
    words = [input().strip() for _ in range(n)]
    step = 0
    while True:
        if len(set(words)) < n or '' in words:
            break
        words = [x[1:] for x in words]
        step += 1
    print(step-1)