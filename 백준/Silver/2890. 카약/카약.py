import sys
input = sys.stdin.readline

r, c = map(int, input().split())

dist = [0]*10  
for _ in range(r):
    line = input().strip()
    for ch in '123456789':
        if ch in line:
            team = int(ch)
            idx_team = line.index(ch) + 2 
            idx_finish = line.index('F')
            dist[team] = idx_finish - idx_team
            break

sorted_dist = sorted(set(dist[1:]))
rank = [0]*10
for i in range(1, 10):
    rank[i] = sorted_dist.index(dist[i]) + 1

for i in range(1, 10):
    print(rank[i])