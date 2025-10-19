# bronzeII_13410
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

result = []
for i in range(1, k+1):
    num = str(n*i)[::-1]
    result.append(int(num))
print(max(result))