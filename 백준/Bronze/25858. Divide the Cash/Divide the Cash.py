n,d=map(int, input().split())
num=[]
for _ in range(n):
    num.append(int(input()))
length=sum(num)
num=[i/length for i in num]

for i in num:
    print(int(i*d))