import sys
input = sys.stdin.readline

t = int(input())
for case in range(1, 1+t):
    n = int(input())
    lines = [tuple(map(int, input().split())) for _ in range(n)]
    
    count = 0
    for i in range(n):
        x = lines[i]
        for j in range(i+1, n):
            y = lines[j]
            if (x[0]>y[0] and x[1]<y[1])\
                or (x[0]<y[0] and x[1]>y[1]):
                    count += 1
    print(f'Case #{case}: {count}')