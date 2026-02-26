import sys
input = sys.stdin.readline

n, m = map(int, input().split())

left = [0] * (n + 1)
for i in range(1, n):
    left[i] = int(input())
bottom = list(map(int, input().split()))
    
    
for r in range(1, n + 1):
    for c in range(1, m + 1):
        ok = True
        
        for i in range(1, n):
            if abs(r - i) + abs(c - 1) != left[i]:
                ok = False
                break
        if not ok:
            continue
        
        for j in range(1, m + 1):
            if abs(r - n) + abs(c - j) != bottom[j - 1]:
                ok = False
                break
        if ok:
            print(r, c)
            sys.exit()
            