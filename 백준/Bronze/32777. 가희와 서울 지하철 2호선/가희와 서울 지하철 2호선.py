import sys
input = sys.stdin.readline

q = int(input())
for _ in range(q):
    a, b = map(int, input().split())
    inner = b - a + (43 if a > b else 0)
    outer = a - b + (43 if a < b else 0)
    
    if inner < outer:
        print("Inner circle line")
    elif inner > outer:
        print("Outer circle line")
    else:
        print("Same")