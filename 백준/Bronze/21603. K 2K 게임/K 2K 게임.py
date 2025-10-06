# bronzeIII_21603
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

result = []
for i in range(1, n+1):
    if i % 10 not in [k%10, (2*k)%10]:
        result.append(i)
print(len(result))
print(*result)