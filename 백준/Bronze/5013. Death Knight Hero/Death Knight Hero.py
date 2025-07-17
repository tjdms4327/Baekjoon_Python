n=int(input())

cnt=0
for _ in range(n):
    if 'CD' not in input():
        cnt+=1
print(cnt)