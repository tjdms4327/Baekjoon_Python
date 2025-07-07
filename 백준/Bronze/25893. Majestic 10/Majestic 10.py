import sys
input=sys.stdin.readline

n=int(input())
for _ in range(n):
    player=list(map(int, input().split()))
    players=sorted(player)
    defalut=''
    if players[-1]<10:
        defalut='zilch'
    elif players[0]>=10:
        defalut='triple-double'
    elif players[-1]>=10 and players[1]<10:
        defalut='double'
    else:
        defalut='double-double'
    print(*player)
    print(defalut+'\n')