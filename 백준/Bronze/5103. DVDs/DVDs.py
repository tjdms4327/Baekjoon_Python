# bronzeII_5103
import sys
input = sys.stdin.readline

while True:
    dvd = input().strip()
    if dvd == '#': break
    
    m, s = map(int, input().split())
    t = int(input())
    for _ in range(t):
        a, x = input().strip().split()
        x = int(x)
    
        if a == 'S':
            s = max(0, s-x)
        else:
            s = min(m, s+x)
            
    print(dvd, s)