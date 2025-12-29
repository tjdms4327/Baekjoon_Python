import sys
input = sys.stdin.readline

a, m = map(int, input().split())

x = 1
while True:
    if a*x % m == 1:
        print(x)
        sys.exit()
        
    x += 1