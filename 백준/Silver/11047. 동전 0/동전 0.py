n,k=map(int, input().split())
values=[int(input()) for _ in range(n)]
values.reverse()

coins=0
for val in values:
    coins+=k//val
    k%=val
print(coins)