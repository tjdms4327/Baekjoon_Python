import sys
input=sys.stdin.readline

lower, higher=map(int, input().split())
n=int(input())
for _ in range(n):
    consumption=int(input())
    if consumption>1000:
        bill=1000*lower + (consumption-1000)*higher
    else:
        bill=consumption*lower
    print(consumption, bill)