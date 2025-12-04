import sys, math
input = sys.stdin.readline

n = int(input())

k = math.ceil(n**0.5)
print((k+2)*'x')
for _ in range(k):
    print('x' + '.'*k + 'x')
print((k+2)*'x')