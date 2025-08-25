import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = list(map(int, input().strip()))
    tot = sum(n) + (n[-3]*100+n[-2]*10+n[-1])*10
    
    if tot >= 10000:
        tot %= 10000
    elif tot < 1000: 
        tot += 1000
    print(f'{tot:04d}')
