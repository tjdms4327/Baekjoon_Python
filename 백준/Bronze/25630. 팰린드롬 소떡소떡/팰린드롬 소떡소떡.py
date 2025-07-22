n=int(input())
s=input()

cnt=0
for i in range(n//2):
    if s[i]!=s[n-1-i]:
        cnt+=1
        #print(s[i], s[n-1-i], '/ cnt:', cnt)
print(cnt)