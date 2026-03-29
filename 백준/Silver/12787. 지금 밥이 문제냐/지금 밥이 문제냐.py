import sys
input = sys.stdin.readline

def trans(s, m):
    if m == 1: # IPv8 → 정수
        lst = list(map(int, s.split('.')))
        
        res = 0
        for x in lst:
            res = (res << 8) + x 
        
        return res
    
    elif m == 2: # 정수 → IPv8
        num = int(s)
        res = []
        
        for i in range(8):
            res.append(str(num & 255)) 
            num >>= 8  
            
        return '.'.join(res[::-1])  


t = int(input())
for _ in range(t):
    m, n = input().strip().split()
    m = int(m)  
    
    print(trans(n, m))