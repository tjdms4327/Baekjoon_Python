import sys, math
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

x = int(input())
result = []
for a in A:
    if math.gcd(x, a) == 1:
        result.append(a)
print(sum(result) / len(result))