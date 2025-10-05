# silverV_7390
import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())
stock_price = [0] + [float(input()) for _ in range(k)]

prefix_sum = [0] * (k+1)
for i in range(1, k+1):
    prefix_sum[i] = prefix_sum[i-1] + stock_price[i]

avg_m = [0] * (k+1)
for i in range(m, k+1):
    avg_m[i] = (prefix_sum[i] - prefix_sum[i - m]) / m
avg_n = [0] * (k+1)
for i in range(n, k+1):
    avg_n[i] = (prefix_sum[i] - prefix_sum[i - n]) / n

result = [''] * (k+1)
for i in range(n, k+1):
    if avg_m[i] < avg_n[i]:
        result[i] = 'bearish'
    else:
        result[i] = 'bullish'
    
    if i == n:  # 첫 번째 날
        if result[i] == 'bullish':
            print(f'BUY ON DAY {i}')
        else:
            print(f'SELL ON DAY {i}')
    else:
        if result[i - 1] == 'bearish' and result[i] == 'bullish':
            print(f'BUY ON DAY {i}')
        elif result[i - 1] == 'bullish' and result[i] == 'bearish':
            print(f'SELL ON DAY {i}')