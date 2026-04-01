import sys
input=sys.stdin.readline

t=int(input().strip())
for _ in range(t):
    s=input().strip()
    half_length=len(s)//2
    if s[half_length-1]==s[half_length]:
        print('Do-it')
    else: print('Do-it-Not')    