import sys
input = sys.stdin.readline

while True:  
    line = list(input().strip().split())
    if line == ['#']:
        break
    
    result = []
    for x in line:
        if len(x) <= 3:
            result.append(x)
        else:
            result.append(x[0] + x[1:-1][::-1] + x[-1])
    print(' '.join(result))