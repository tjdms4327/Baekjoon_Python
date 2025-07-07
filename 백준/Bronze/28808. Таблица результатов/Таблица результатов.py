n,m=map(int, input().split())

num=0
for _ in range(n):
    solve=input()
    if '+' in solve:
        num+=1
print(num)