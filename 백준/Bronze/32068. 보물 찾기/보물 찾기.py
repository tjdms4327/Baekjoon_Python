import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    l, r, s = map(int, input().split())
    
    right = 2*(r-s)
    left = 2*(s-l) + 1
    print(min(right, left))