# bronzeII_23320
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
x, y = map(int, input().split())

x_count = int(n * x / 100)
y_count = sum(1 for i in A if i >= y)
print(x_count, y_count)