import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    voted = [int(input()) for _ in range(n)] 
    
    winner = max(voted)
    winner_idx = [idx+1 for idx in range(n) if voted[idx]==winner]
    tot = sum(voted)
    
    if len(winner_idx) != 1:
        print('no winner')
    elif winner*2 > tot:
        print(f'majority winner {winner_idx[0]}')
    else:
        print(f'minority winner {winner_idx[0]}')