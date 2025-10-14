# bronzeII_2028
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = input().strip()
    len_n = len(n)
    
    if str(int(n)**2)[-len_n:] == n:
        print('YES')
    else:
        print('NO')