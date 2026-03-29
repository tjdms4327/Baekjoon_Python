import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s, p = input().strip().split()
    n = len(p)
    
    time = 0
    cur = 0
    while cur < len(s):
        if s[cur:cur+n] == p:
            cur += n
        else:
            cur += 1
        time += 1
        
    print(time)