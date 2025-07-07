import sys
input=sys.stdin.readline

n=int(input())
s=list(input().strip().upper())
for i in range(n):
    if s[i]=='I':
        s[i]=s[i].lower()
print(''.join(s))