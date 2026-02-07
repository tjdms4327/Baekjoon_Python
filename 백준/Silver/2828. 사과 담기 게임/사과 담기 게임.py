import sys
input = sys.stdin.readline

n, m = map(int, input().split())
j = int(input())
apples = [int(input()) for _ in range(j)]

s, e = 1, m
distance = 0
for x in apples:
    if s <= x <= e:
        continue
    elif x < s:
        d = s-x
        s = x
        e = s+m-1
    else:
        d = x-e
        e = x
        s = e-m+1
    distance += d

print(distance)