import sys
input = sys.stdin.readline

k = int(input())
for case in range(1, 1+k):
    n, m = map(int, input().split())
    coordinates = [tuple(map(int, input().split())) for _ in range(n)]
    
    user = list(map(int, input().split()))
    x0, y0 = coordinates[user[0]-1]
    x1, y1 = coordinates[user[0]-1]
    for i in user[1:]:
        x, y = coordinates[i-1]
        x0 = min(x0, x)
        x1 = max(x1, x)
        y0 = min(y0, y)
        y1 = max(y1, y)
    
    count = 0
    for x, y in coordinates:
        if x0<=x<=x1 and y0<=y<=y1:
            count += 1
    
    print(f'Data Set {case}:')
    print(count, '\n')