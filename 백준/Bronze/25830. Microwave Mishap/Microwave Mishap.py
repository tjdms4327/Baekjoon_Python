import sys
input = sys.stdin.readline

m,s = map(int, input().split(':'))
seconds = (3600*m + 60*s) - (60*m + s)

h = seconds //3600
m = (seconds%3600) // 60
s = (seconds % 3600) % 60
print(f'{h:02d}:{m:02d}:{s:02d}')