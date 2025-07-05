def winner(one, two, win1, win2):
    if one==two:
        pass
    elif (one=='R' and two=='P') or (one=='P' and two=='S') or (one=='S' and two=='R'):
        win2+=1
    else:
        win1+=1
    return win1, win2
    
t=int(input())
for _ in range(t):
    n=int(input())
    win1, win2=0,0
    for _ in range(n):
        one, two=input().split()
        win1, win2=winner(one, two, win1, win2)
    if (win1==win2):
        print('TIE')
    elif (win1>win2):
        print('Player 1')
    else:
        print('Player 2')