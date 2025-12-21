import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip()
    
    n = len(s)
    best = s
    for i in range(1, n):
        new_s = s[i:]+s[:i]
        
        if best > new_s:
            best = new_s
    print(best)