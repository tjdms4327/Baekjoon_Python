# bronzeI_32343
import sys, math
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())

diff = min(a+b, 2*n - (a+b))
ans = ((1 << diff) - 1) << (n - diff)
print(ans)