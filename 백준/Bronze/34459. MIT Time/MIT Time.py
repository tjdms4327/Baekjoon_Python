import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    if n <= 5:
        print('MIT time')
    else:
        k = 1
        while 5**k < n:
            k += 1
        print(f'MIT^{k} time')