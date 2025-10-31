# silverII_26072
import sys
input = sys.stdin.readline

def balance(X):
    left = sum(w[i] * (X - x[i]) for i in range(n) if x[i] < X)
    right = sum(w[i] * (x[i] - X) for i in range(n) if x[i] > X)
    return left - right

n, l = map(int, input().split())
x = list(map(int, input().split()))
w = list(map(int, input().split()))

le, ri = 0.0, l
epsilon = 1e-7
while ri - le > epsilon:
    mid = (le+ri) / 2
    if balance(mid) > 0:
        ri = mid
    else:
        le = mid
print(f"{(le + ri) / 2:.10f}")
