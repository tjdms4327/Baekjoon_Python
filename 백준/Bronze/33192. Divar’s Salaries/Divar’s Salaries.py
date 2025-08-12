import sys
input=sys.stdin.readline

n=int(input())
for _ in range(n):
    x, k, h=map(int, input().split())

    price=x
    weekday=k-h
    if weekday<=140:
        price*=(weekday+2*h)
    else:
        price*=((weekday-140)*1.5+140+2*h)
    print(f'{int(price):,}')