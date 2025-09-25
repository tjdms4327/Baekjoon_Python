# bronzeII_4581
import sys
input = sys.stdin.readline

while True:  
    s = input().strip()
    if s == '#': break
    
    Y, N = s.count('Y'), s.count('N')
    if s.count('A') >= len(s)/2:
        print('need quorum')
    elif Y > N:
        print('yes')
    elif Y < N:
        print('no')
    else:
        print('tie')