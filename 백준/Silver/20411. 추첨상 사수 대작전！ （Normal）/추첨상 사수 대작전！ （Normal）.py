import sys
input = sys.stdin.readline

m, seed, x1, x2 = map(int, input().split())

# x2-x1 = a(x1-seed) (mod m)
inv = pow((x1-seed)%m, m-2, m) # (x1-seed) mod m 의 역원

a = ((x2-x1)*inv) % m
c = (x1 - a*seed) % m
print(a, c)