import sys
input = sys.stdin.readline

k, s = map(int, input().split())

x = s // k
y = s % k
print(x + y)