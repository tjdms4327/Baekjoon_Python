import sys
input = sys.stdin.readline

n, m, t, x, y = map(int, input().split())
P = [0] + [int(input()) for _ in range(m)]

scores = [0]*(n+1)
log = {}
for _ in range(y):
    line = input().strip().split()
    
    time = int(line[0])
    idx = int(line[1])
    problem = int(line[2])
    
    if line[-1]=='open':
        log[(idx, problem)] = [time, 0]
    elif line[-1]=='correct':
        score = P[problem] - (time - log[(idx, problem)][0]) - 120*log[(idx, problem)][1]
        scores[idx] += max(score, x)
    elif line[-1]=='incorrect':
        log[(idx, problem)][1] += 1

print(*scores[1:], sep='\n')