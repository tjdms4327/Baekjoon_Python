import sys
input=sys.stdin.readline

s=input().strip()
missing=''
for i in "UAPC":
    if i not in s:
        missing+=i
print(missing)