import math

n = int(input())
result = n
for p in range(2, int(math.sqrt(n))+1):
    if n % p == 0:
        result = result - result / p
        while n % p == 0:
            n /= p
if n > 1: # 제곱급까지만 탐색했으므로 1개의 소인수 누락되는 케이스
    result -= result / n

print(int(result))