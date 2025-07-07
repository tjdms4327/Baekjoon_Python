scicomlove=list('SciComLove')
s=input()
cnt=0
for i in range(10):
    if s[i]!=scicomlove[i]: cnt+=1
print(cnt)