import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    card = sorted(list(input().strip().split()))
    remember = sorted(list(input().strip().split()))
    
    if card == remember:
        print('NOT CHEATER')
    else:
        print('CHEATER')
        