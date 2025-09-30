# bronzeIII_32046
import sys
input = sys.stdin.readline

while True:  
    n = int(input())
    if n == 0: break
    
    snack = list(map(int, input().split()))
    price = 0
    for i in snack:
        if price + i <= 300:
            price += i
    print(price)