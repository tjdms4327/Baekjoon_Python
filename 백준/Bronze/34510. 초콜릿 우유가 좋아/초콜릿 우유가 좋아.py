# bronzeII_34510
import sys
input = sys.stdin.readline

h1, h2, h3 = map(int, input().split())
n = int(input())

height = h3*n+h2*(n//2)
if n % 2 == 1:
    height += (h2+h1)
print(height)