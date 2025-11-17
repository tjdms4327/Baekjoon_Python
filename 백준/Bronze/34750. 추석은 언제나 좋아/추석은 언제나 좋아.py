# bronzeIV_34750
import sys
input = sys.stdin.readline

n = int(input())
if n >= 1000000:
    give = n*0.2
elif n >= 500000:
    give = n*0.15
elif n >= 100000:
    give = n*0.1
else:
    give = n*0.05

give = int(give)
print(give, n-give)