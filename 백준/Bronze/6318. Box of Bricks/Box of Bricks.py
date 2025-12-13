import sys
input = sys.stdin.readline

case = 0
while True:   
    n = int(input())
    if n == 0:
        break
    
    case += 1
    H = list(map(int, input().split()))
    avg = sum(H) // n
    result = sum(h-avg for h in H if h>avg)
    print(f'Set #{case}\nThe minimum number of moves is {result}.\n')