import sys
input = sys.stdin.readline

n = int(input())
max_win = 0
current = 0
for _ in range(n):
    s, t = map(int, input().split())
    
    if s > t:     
        current += 1
    else:         
        current = 0
    max_win = max(max_win, current)
print(max_win)