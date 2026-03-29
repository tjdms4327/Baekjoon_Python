import sys, math
input = sys.stdin.readline

n, m = map(int, input().split(':'))

GCD = math.gcd(n, m)
print(f'{n//GCD}:{m//GCD}')