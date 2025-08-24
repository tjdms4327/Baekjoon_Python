import sys
input = sys.stdin.readline

p = int(input())

C = [0, 0, 0, 0]
for _ in range(p):
    g, c, n= map(int, input().split())
    if g == 1:
        C[3] += 1
    else:
        if c in [1, 2]:
            C[0] += 1
        elif c == 3:
            C[1] +=1
        else:
            C[2] += 1

print(*C, sep='\n')