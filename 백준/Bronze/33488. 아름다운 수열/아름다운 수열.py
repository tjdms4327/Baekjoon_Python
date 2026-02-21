import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    if n == 3:
        print("YES")
        print("2 1 3")
        continue
    
    print("YES")
    print(*range(1, n+1))