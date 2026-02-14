import sys
input = sys.stdin.readline

a, b = map(int, input().split())
r = int(input())

coord = []
t = 0
while (a, b) not in coord:
    coord.append((a, b))
    if (a+1)+(b+1) < r:
        a += 1
        b += 1
    else:
        a //= 2
        b //= 2
    t += 1
    
print(t)