n,m,k=map(int, input().split())
team=min(n//2, m)
remain=n+m-3*team

if k>remain:
    need=k-remain
    team-=(need+2)//3
team=max(team,0)
print(team)