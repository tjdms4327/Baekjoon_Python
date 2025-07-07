n=int(input())
s=input()
t=input()

diff=0
for i in range(n):
    if s[i]!=t[i]:
        diff+=1
print(diff)