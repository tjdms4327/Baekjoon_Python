# bronzeI_1816
import sys
input = sys.stdin.readline

LIMIT = 10**6
is_prime = [True] * (LIMIT + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(LIMIT ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, LIMIT + 1, i):
            is_prime[j] = False
primes = [i for i, val in enumerate(is_prime) if val]


def propriate(num):
    for p in primes:
        if p * p > num:
            break
        if num % p == 0:
            return "NO"
    return "YES"

n = int(input())
for _ in range(n):
    num = int(input())
    print(propriate(num))
