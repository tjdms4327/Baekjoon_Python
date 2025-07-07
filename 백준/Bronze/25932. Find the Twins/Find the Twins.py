import sys
input=sys.stdin.readline

n=int(input())
for _ in range(n):
    player=list(map(int, input().split()))
    find='none'
    if 18 in player and 17 in player:
        find='both'
    elif 18 in player:
        find='mack'
    elif 17 in player:
        find='zack'
    print(*player)
    print(find+'\n')