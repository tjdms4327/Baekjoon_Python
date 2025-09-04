import sys
input = sys.stdin.readline

for case in range(1, int(input())+1):
    xy = list(map(float, input().split()))
    scores = []
    for i in range(0, 12, 2):
        d = (xy[i]**2 + xy[i+1]**2) ** 0.5
        if d <=3: scores.append(100)
        elif d<=6: scores.append(80)
        elif d<=9: scores.append(60)
        elif d<=12: scores.append(40)
        elif d<=15: scores.append(20)
        else: scores.append(0)
    first, second = sum(scores[:3]), sum(scores[3:])
    print(f'SCORE: {first} to {second}, ', end='')
    if first > second: print('PLAYER 1 WINS.')
    elif first == second: print('TIE.')
    else: print('PLAYER 2 WINS.')