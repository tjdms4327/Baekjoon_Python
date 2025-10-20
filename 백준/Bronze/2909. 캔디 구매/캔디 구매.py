# bronzeII_2909
import sys
input = sys.stdin.readline

c, k = map(int, input().split())

money = 10**k
c += 5*(money//10)
print(c//money * money)