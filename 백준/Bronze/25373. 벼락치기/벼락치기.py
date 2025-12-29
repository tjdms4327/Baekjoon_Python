import sys, math
input = sys.stdin.readline

n = int(input())

x = 0
if n > 7*8//2:
    print((n-1)//7 + 4)
    sys.exit()
else:
    for i in range(1, 8):
        if (n*2 <= i*i+i):
            x = i
            break
print(x)