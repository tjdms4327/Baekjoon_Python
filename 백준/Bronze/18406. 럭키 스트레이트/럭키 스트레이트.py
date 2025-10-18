# bronzeII_18406
import sys
input = sys.stdin.readline

n = list(map(int, input().strip()))
len_n = len(n)

half = len_n // 2
if sum(n[:half]) * 2 == sum(n):
    print('LUCKY')
else:
    print('READY')