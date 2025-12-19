import sys
input = sys.stdin.readline

while True:
    line, z = input().strip().split()
    if line == '#' and z == '0':
        break
    
    z = int(z)
    p = int(input())
    s = int(input())
    for _ in range(s):
        left, wait = map(int, input().split())
    
        p = max(p-left, 0)
        p = min(z, p+wait)
        
    print(line, p)