import sys
input=sys.stdin.readline

def win_a(a):
    if a==0 or a>21:
        return 0
    elif a==1:
        return 500
    elif a<=3:
        return 300
    elif a<=6:
        return 200
    elif a<=10:
        return 50
    elif a<=15:
        return 30
    return 10
def win_b(b):
    if b==0 or b>31:
        return 0
    elif b==1:
        return 2**9
    elif b<=3:
        return 2**8
    elif b<=7:
        return 2**7
    elif b<=15:
        return 2**6
    return 2**5

t=int(input())
for _ in range(t):
    a,b=map(int, input().split())
    tot=win_a(a)+win_b(b)
    print(tot*10000)