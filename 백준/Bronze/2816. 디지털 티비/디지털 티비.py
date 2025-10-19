# bronzeI_2816
import sys
input = sys.stdin.readline

n = int(input())
S = [input().strip() for _ in range(n)]

kbs1 = S.index('KBS1')
kbs2 = S.index('KBS2')

print('1' * kbs1 + '4' * kbs1, end='')
if kbs2 < kbs1:
    kbs2 += 1
print('1'*kbs2 + '4'*(kbs2-1))