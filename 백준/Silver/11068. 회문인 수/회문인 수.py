import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    if str(n) == str(n)[::-1]:
        print(1)
        continue
    
    for b in range(2, 65):
        if b == 10:
            continue
        
        x = n
        ok = False
        result = []
        while x >= 1:
            result.append(x%b)
            x //= b
    
        if result == result[::-1]:
            ok = True
            print(1)
            break
        
    if not ok:
        print(0)