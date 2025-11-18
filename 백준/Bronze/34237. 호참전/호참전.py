# bronzeII_34237
import sys
input = sys.stdin.readline

tiger, game = map(int, input().split())

bettings = [tuple(map(int, input().split())) for _ in range(tiger)]
for _ in range(game):
    g, x, y = map(int, input().split())
    count = 0
    for a, b in bettings:
        if x <= a and y <= b and a+b <= g:
            count += 1
    print(count)