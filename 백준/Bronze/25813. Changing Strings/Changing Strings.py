import sys
input = sys.stdin.readline

s = input().strip()

length = len(s)
u_idx = s.index('U')
f_idx = s.rindex('F')

print('-'*u_idx + 'U' 
      + 'C'*(f_idx- u_idx - 1) + 'F'
      + '-'*(length-1 - f_idx))