t=int(input())
change={}
for _ in range(t):
    c, bi=input().split()
    change[bi]=c

s=input() ; length=len(s)
for i in range(0, length, 4):
    chunk=s[i:i+4]
    if chunk in change:
        print(change[chunk], end='')
    else:
        print('?', end='')