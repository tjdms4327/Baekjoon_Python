import sys
input = sys.stdin.readline

bills = [1, 5, 10, 20, 50, 100]
count = list(map(int, input().split()))

bags = [bills[i]*count[i] for i in range(6)]

max_v = 0
select = 0
for idx, x in enumerate(bags):
    if max_v <= x:
        select = idx
        max_v = x
print(bills[select])