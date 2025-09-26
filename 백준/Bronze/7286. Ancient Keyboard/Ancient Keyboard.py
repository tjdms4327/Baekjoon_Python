# bronzeII_7286
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    start, end = 1001, -1
    time = [0] * (1001)
    for _ in range(n):
        x, a, b = input().strip().split()
        a = int(a) ; b = int(b)
        
        start = min(start, a)
        end = max(end, b)
        for J in range(a, b):
            time[J] += 1
    
    for i in time[start:end]:
        if i > 0:
            print(chr((i - 1) % 26 + ord('A')), end='')
    print()