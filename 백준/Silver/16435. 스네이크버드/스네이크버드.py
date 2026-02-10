import sys
input = sys.stdin.readline

n, l = map(int, input().split())
H = list(map(int, input().split()))
H.sort()

for h in H:
    if l >= h:
        l += 1
    else:
        break
    
print(l)