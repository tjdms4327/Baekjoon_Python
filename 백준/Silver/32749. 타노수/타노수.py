import sys
input = sys.stdin.readline

n, t = map(int, input().split())
x = input().strip()

length = 2 ** n
for _ in range(t):
    length //= 2

result = ''
for i in range(0, len(x), length): 
    result = max(result, x[i:i+length])

print(result)
