import sys
input = sys.stdin.readline

coins = []
for i in range(1, 150):
    coins.extend([i]*i)

while True:
    n = int(input())
    if n == 0:
        break
    
    coin = sum(coins[:n])
    print(n, coin)