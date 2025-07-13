import sys
input=sys.stdin.readline

s=set(input().strip()) # id
t=input().strip() # 문자열
for i in s:
    t=t.replace(i, '')
print(t)