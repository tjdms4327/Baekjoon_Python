# bronzeII_10708
import sys
input = sys.stdin.readline

n = int(input())
game = int(input())
targets = list(map(int, input().split()))

scores = [0] * (n+1)
for i in range(game):
    write = [0] + list(map(int, input().split()))
    
    target = targets[i]
    for j in range(1, 1+n):
        if write[j] == target:
            scores[j] += 1
        else:
            scores[target] += 1

print(*scores[1:], sep='\n')
    