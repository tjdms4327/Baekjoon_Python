n=int(input())
winner_score=0
for _ in range(n):
    score=list(map(int, input().split()))
    trick_s=sorted(score[2:])
    player=max(score[:2])+sum(trick_s[-2:])
    
    if player>=winner_score:
        winner_score=player
print(winner_score)