# bronzeII_28236
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

winner, min_move = -1, float('inf')
for i in range(1, k+1):
    f, d = map(int, input().split())
    
    down = f - 1
    side = m - (d-1)
    sum_move = down + side
    
    if min_move > sum_move:
        winner = i
        min_move = sum_move

print(winner)