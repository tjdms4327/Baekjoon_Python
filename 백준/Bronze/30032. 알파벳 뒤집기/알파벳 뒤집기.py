# bronzeIII_30032
import sys
input = sys.stdin.readline

mapping_d1 = {'d':'q', 'q':'d', 'b':'p', 'p':'b'}
mapping_d2 = {'d':'b', 'b':'d', 'q':'p', 'p':'q'}

n, d = map(int, input().split())
for _ in range(n):
    s = input().strip()
    if d == 1:
        for i in s:
            print(mapping_d1[i], end='')
    else:
        for i in s:
            print(mapping_d2[i], end='')
    print()