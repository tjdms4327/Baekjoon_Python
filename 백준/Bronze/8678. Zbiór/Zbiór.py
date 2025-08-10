import sys
input=sys.stdin.readline

t=int(input())
for i in range(t):
    a, b=map(int, input().split())
    if b%a==0:
        print('TAK')
    else: print('NIE')