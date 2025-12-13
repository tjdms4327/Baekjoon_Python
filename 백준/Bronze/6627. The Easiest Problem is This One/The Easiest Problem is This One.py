import sys
input = sys.stdin.readline

while True:
    n = input().strip()
    if n == '0':
        break
    
    Sn = sum(list(map(int, n)))
    p = 11
    while sum(list(map(int, str(int(n)*p)))) != Sn:
        p += 1
    print(p)