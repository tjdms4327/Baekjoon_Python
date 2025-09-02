import sys
input = sys.stdin.readline

a, b, c = input().strip().split()
s = a
s += ("'" + b[-1] if a[-1] == b[0] else b)
s += ("'" + c[-1] if b[-1] == c[0] else c)
print(s)