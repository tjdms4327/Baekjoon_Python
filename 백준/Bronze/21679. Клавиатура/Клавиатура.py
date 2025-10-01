# bronzeIII_21679
import sys
input = sys.stdin.readline

n = int(input())
key = [0] + list(map(int, input().split()))
k = int(input())
push = list(map(int, input().split()))

for i in range(1, n+1):
    key[i] -= push.count(i)
for i in key[1:]:
    print('yes' if i < 0 else 'no')