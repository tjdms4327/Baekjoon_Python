import sys
input=sys.stdin.readline

t=int(input().strip())
for _ in range(t):
    n,m,l=map(int, input().strip().split())
    Si=list(map(int, input().strip().split()))
    real_Si=list(filter(lambda x: x!=-1, Si))
    
    x=max(l, m-min(real_Si, default=m)) # default=m은 시간 내에 1문제 남기고 다 푼 사람이 없다는 거
    if x==1: print(f'The scoreboard has been frozen with {x} minute remaining.')
    else: print(f'The scoreboard has been frozen with {x} minutes remaining.')