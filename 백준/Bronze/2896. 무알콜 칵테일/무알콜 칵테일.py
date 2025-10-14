# bronzeI_2896
import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
i, j, k = map(int, input().split())

x = min(a/i, b/j, c/k)
rem_a = a - i*x
rem_b = b - j*x
rem_c = c - k*x
print(rem_a, rem_b, rem_c)