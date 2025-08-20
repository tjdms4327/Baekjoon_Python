t = int(input())
for _ in range(t):
    n = int(input())
    profit = 0
    for _ in range(n):
        each_day = list(map(int, input().split()))
        if max(each_day) > 0:
            profit += max(each_day)
    print(profit)