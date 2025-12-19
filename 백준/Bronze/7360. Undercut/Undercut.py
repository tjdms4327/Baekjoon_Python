import sys
input = sys.stdin.readline

while True:  
    n = int(input())
    if n == 0:
        break
    
    card1 = list(map(int, input().split()))
    card2 = list(map(int, input().split()))
    
    player1, player2 = 0, 0
    for i in range(n):
        x, y = card1[i], card2[i]
        if x==y:
            continue
        elif abs(x - y) == 1:
            if set([x, y]) == set([1, 2]):
                sum = 6
            else:
                sum = x+y
            if x > y:
                player2 += sum
            else:
                player1 += sum
        else:
            if x > y:
                player1 += x
            else:
                player2 += y
    
    print(f'A has {player1} points. B has {player2} points.\n')