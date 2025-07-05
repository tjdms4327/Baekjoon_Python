import sys
input = sys.stdin.readline

s=input()
cambridge=['C','A','M','B','R','I','D','G','E']
for i in cambridge:
    s=s.replace(i,'')
print(s)