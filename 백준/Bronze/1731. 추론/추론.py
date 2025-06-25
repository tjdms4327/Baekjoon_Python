n=int(input())
num=[]
for _ in range(n):
    num.append(int(input()))

if num[1]-num[0]==num[2]-num[1]:
    print(num[-1]+num[1]-num[0])
else:
    print(num[-1]*(num[1]//num[0]))