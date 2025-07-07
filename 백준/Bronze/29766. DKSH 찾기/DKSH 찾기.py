s=input()

c=0
for i in range(len(s)):
    if s[i:i+4]=='DKSH':
        c+=1
        i+=4
print(c)