import sys
input=sys.stdin.readline

t=int(input())
s=int(input())
h=int(input())

for _ in range(t):
    print('*'+' '*s+'*'+' '*s+'*')
print('*'*3+'*'*s*2)
for _ in range(h):
    print(' '*(1+s)+'*')