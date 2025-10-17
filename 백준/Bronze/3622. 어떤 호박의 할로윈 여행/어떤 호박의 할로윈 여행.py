# bronzeII_3622
import sys
input = sys.stdin.readline

A, a, B, b, P = map(int, input().split())
if (P>=A and a>=B) or (P>=B and b>=A) or (P>= A+B):
    print('Yes')
else:
    print('No')