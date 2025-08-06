import sys
input=sys.stdin.readline

n=int(input())
for _ in range(n):
    s=input().strip()
    if (int(s[:2])**2+int(s[2:])**2)%7==1:
        print('YES')
    else: print('NO')