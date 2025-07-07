n=int(input())
for _ in range(n):
    coins=list(map(int, input().split()))
    print('Denominations:',*coins[1:], sep=' ')

    out='Good coin denominations!'
    for i in range(2,coins[0]+1):
        if coins[i]<coins[i-1]*2:
            out='Bad coin denominations!'
            break
    print(out)
    print()