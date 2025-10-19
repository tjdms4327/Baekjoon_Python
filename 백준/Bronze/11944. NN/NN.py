# bronzeII_11944
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

result = str(n) * n
if len(result) > m:
    print(result[:m])
else:
    print(result)