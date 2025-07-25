n=int(input())
s=list(input())
for i in range(n):
    if s[i]=='?':
        if s[n-1 - i]!='?':
            s[i]=s[n-1 - i]
        else:
            s[i]='a' ; s[n-i-1]='a'
print(*s, sep='')