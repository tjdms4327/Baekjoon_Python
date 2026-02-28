import sys
input = sys.stdin.readline

n, m = map(int, input().split())

adj = [set() for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].add(b)
    adj[b].add(a)


teams = []
for player in range(1, n+1):
    placed = False
    
    for team in teams:
        conflict = False
        for member in team:
            if member in adj[player]:
                conflict = True
                break
        
        if not conflict:
            team.append(player)
            placed = True
            break
    
    if not placed:
        teams.append([player])

print(len(teams))
for team in teams:
    print(*team)