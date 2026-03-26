import sys
input = sys.stdin.readline

t = int(input())

res = []
for _ in range(t):
    n = int(input().strip()) 
    
    if n <= 2:
        print(1)
    else:
        print(3)