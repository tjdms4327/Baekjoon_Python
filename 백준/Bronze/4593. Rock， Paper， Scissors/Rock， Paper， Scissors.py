# bronzeII_4593
import sys
input = sys.stdin.readline

while True:
    one, two = input().strip(), input().strip()
    if one == two == 'E': break
    
    score1, score2 = 0, 0
    length = len(one)
    for i in range(length):
        if one[i] == two[i]:
            continue
        elif (one[i] == 'R' and two[i] == 'S') or (one[i] == 'S' and two[i] == 'P') or (one[i] == 'P' and two[i] == 'R'):
            score1 += 1
        else:
            score2 += 1
    print(f'P1: {score1}')
    print(f'P2: {score2}')