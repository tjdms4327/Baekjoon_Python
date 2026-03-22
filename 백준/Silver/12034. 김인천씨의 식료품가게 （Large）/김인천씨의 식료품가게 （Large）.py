import sys
input = sys.stdin.readline

t = int(input())
for case in range(1, 1+t):
    n = int(input())
    P = list(map(int, input().split()))
    P.sort()
    
    discount = []
    while P:
        d = P[0] 
        if 4 * d % 3 == 0:
            normal = 4 * d // 3
            if normal in P:
                discount.append(d)
                P.remove(d)
                P.remove(normal)
            else:
                P.pop(0)
        else:
            P.pop(0)
    
    discount.sort()
    print(f"Case #{case}: {' '.join(map(str, discount))}")