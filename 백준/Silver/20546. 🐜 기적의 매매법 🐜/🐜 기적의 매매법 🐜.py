import sys
input = sys.stdin.readline

cash = int(input())
X = list(map(int, input().split()))

jun = cash
jun_stock = 0
for x in X:
    buy = jun // x
    jun_stock += buy
    jun -= buy * x
jun += jun_stock * X[-1]

sung = cash
sung_stock = 0
for i in range(len(X)):
    if i >= 3:
        if X[i-3] < X[i-2] < X[i-1]:
            sung += sung_stock * X[i]
            sung_stock = 0
        elif X[i-3] > X[i-2] > X[i-1]:
            buy = sung // X[i]
            sung_stock += buy
            sung -= buy * X[i]
sung += sung_stock * X[-1]


if jun > sung:
    print("BNP")
elif jun < sung:
    print("TIMING")
else:
    print("SAMESAME")