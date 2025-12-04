import sys
input = sys.stdin.readline

def star(n):
    for i in range(n-1):
        print(' '*i + '*' + ' '*(2*(n-1-i)-1) + '*')
    print(' '*(n-1) + '*')        

N = list(map(int, input().split()))
for n in N:
    star(n)