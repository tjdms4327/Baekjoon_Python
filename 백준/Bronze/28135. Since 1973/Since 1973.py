num=int(input())
cur=0
cnt=0
for i in range(1, num+1):
    cur+=1
    cnt+=1
    if cur==num: break
    if '50' in str(i):
        cnt+=1
    
print(cnt)