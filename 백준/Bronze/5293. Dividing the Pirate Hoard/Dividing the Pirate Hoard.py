import sys
input = sys.stdin.readline

m, n = map(int, input().split())

result = []
for _ in range(n):
    x = m//n
    y = m%n
    result.append(x+y)
    
    m -= (x+y)

print(*result)
print(m)