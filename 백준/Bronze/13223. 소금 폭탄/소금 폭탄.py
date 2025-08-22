import sys
input = sys.stdin.readline

h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))


t1 = h1*3600 + m1*60 + s1
t2 = h2*3600 + m2*60 + s2

delta = t2 - t1
if delta <= 0:
    delta += 24*3600

h, rem = divmod(delta, 3600)
m, s = divmod(rem, 60)

print(f'{h:02d}:{m:02d}:{s:02d}')