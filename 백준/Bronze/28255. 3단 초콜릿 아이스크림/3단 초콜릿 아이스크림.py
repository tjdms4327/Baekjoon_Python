import sys, math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip()
    n = len(s)
    
    s_ = s[:math.ceil(n/3)]
    
    cand = [
        s_ + s_[::-1] + s_ , 
        s_ + s_[::-1][1:] + s_ , 
        s_ + s_[::-1] + s_[1:] , 
        s_ + s_[::-1][1:] + s_[1:]
    ]
    
    if s in cand:
        print(1)
    else:
        print(0)