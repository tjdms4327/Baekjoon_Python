import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    j, n = map(int, input().split())
    
    box = []
    for _ in range(n):
        r, c = map(int, input().split())
        box.append(r*c)
    box.sort(reverse=True)
    
    count = 0
    for b in box:
        if b < j:
            j -= b
            count += 1
        else:
            count += 1
            break
    print(count)