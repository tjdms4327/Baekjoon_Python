import sys
input = sys.stdin.readline

def getDivisor(n):
    divisors = set()
    for i in range(2, int(n**1/2)+1):
        if n%i == 0:
            divisors.add(i)
            divisors.add(n//i)
    return divisors

t = int(input())
for _ in range(t):
    n = int(input())
    sum_divisor = sum(getDivisor(n)) + 1

    if sum_divisor == n:
        print(f'{n} is a perfect number.\n')
    elif sum_divisor < n:
        print(f'{n} is a deficient number.\n')
    else:
        print(f'{n} is an abundant number.\n')