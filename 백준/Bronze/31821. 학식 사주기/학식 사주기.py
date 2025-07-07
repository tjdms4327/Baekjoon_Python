N=int(input())
price=[None]
for _ in range(N):
    price.append(int(input()))

M=int(input())
tot=0
for _ in range(M):
    num=int(input())
    tot+=price[num]
print(tot)