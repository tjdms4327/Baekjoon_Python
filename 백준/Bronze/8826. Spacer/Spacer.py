import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    x = abs(s.count('W') - s.count('E'))
    y = abs(s.count('N') - s.count('S'))
    print(x + y)