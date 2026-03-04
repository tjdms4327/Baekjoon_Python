import sys
input = sys.stdin.readline

x, y = map(int, input().split())

x = bin(x)[2:].zfill(16)
y = bin(y)[2:].zfill(16)

result = ''
for i in range(16):
    result += x[i] + y[i]
print(int(result, 2))