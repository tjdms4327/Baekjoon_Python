# bronzeII_11328
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s1, s2 = input().strip().split()
    s1 = sorted(list(s1))
    s2 = sorted(list(s2))
    
    if s1 == s2:
        print('Possible')
    else:
        print('Impossible')