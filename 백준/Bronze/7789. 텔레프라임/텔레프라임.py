import sys, math
input = sys.stdin.readline

def is_prime(n):
    prime = True
    for i in range(2, n):
        if (n % i == 0):
            prime = False
            break
    return prime

a, b = input().strip().split()
if is_prime(int(a)) and is_prime(int(a) + int(b)*(10**len(a))):
    print('Yes')
else:
    print('No')