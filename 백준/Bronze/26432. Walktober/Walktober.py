import sys
input = sys.stdin.readline

t = int(input())
for case in range(1, 1+t):
    m, n, p = map(int, input().split())
    scores = [list(map(int, input().split())) for _ in range(m)]
    
    john = scores[p-1]
    day_score = [max(col) for col in zip(*scores)]
    
    count = 0
    for i in range(n):
        diff = day_score[i] - john[i]
        if diff > 0:
            count += diff
    print(f'Case #{case}: {count}')