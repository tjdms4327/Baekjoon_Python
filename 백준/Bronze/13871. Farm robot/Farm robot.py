# bronzeIII_13871
import sys
input = sys.stdin.readline

n, c, s = map(int, input().split())
X = list(map(int, input().split()))

move = [1]
for x in X:
    if x == 1:
        move.append(move[-1] % n + 1)
    else: 
        move.append((move[-1] - 2) % n + 1)
print(move.count(s))