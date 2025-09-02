import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())

if a+c == b+d:
    print('Either')
elif a+c < b+d:
    print('Hanyang Univ.')
else:
    print('Yongdap')