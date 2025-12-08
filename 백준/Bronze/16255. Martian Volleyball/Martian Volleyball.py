import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k, x, y = map(int, input().split())
    
    a = max(x, y)
    b = min(x, y)
    if a < k:
        if k-b >= 2:
            temp = k-a
        else:
            temp = b-a+2
    else:
        temp = 2 - (a-b)
    print(temp)