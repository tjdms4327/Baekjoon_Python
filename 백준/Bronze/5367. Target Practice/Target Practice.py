import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    if i in [0, n-1]:
        print('|' + '-'*(n-2) + '|')
    elif i < n//2:
        print('|' + ' '*(i-1) + '*' + ' '*(n-2*i-2) + '*' + ' '*(i-1) + '|')
    elif i == n//2:
        print('|' + ' '*((n-2)//2) + '*' + ' '*((n-2)//2) + '|')
    else:
        x = n-1 - i
        print('|' + ' '*(x-1) + '*' + ' '*(n-2*x-2) + '*' + ' '*(x-1) + '|')