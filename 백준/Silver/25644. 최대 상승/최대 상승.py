import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

min_price = A[0]  
max_profit = 0
for price in A[1:]:
    profit = price - min_price
    max_profit = max(max_profit, profit)
    min_price = min(min_price, price) 

print(max_profit)