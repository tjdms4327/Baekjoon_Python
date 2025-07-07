import sys
input=sys.stdin.readline

n=int(input())
prizes=list(map(int, input().split()))
if sum(prizes)%3==0:
    print('yes')
else:
    print('no')