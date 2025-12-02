import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    
    if x == X or y == Y:
        print(0)
    else:
        print(1)
        