# bronzeIII_29657
import sys
input = sys.stdin.readline

a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
h, m, s = map(int, input().split())

total_seconds = h*(b1*c1) + m*c1 + s
h2 = total_seconds // (b2 * c2)
m2 = (total_seconds // c2) % b2
s2 = total_seconds % c2
print(h2, m2, s2)