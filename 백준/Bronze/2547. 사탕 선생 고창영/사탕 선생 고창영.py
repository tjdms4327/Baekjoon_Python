t=int(input())
for _ in range(t):
    empty=input()
    n=int(input())
    candy=[int(input()) for _ in range(n)]
    if sum(candy)%n==0:
        print('YES')
    else:
        print('NO')