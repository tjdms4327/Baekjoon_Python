import sys
input = sys.stdin.readline

h = int(input())
M = int(input())

def altitude(h, M):
    for t in range(1, M+1):
        a = (-1)*6*t**4+h*t**3+2*t**2+t
        if a <= 0:
            return t
    return 0

time = altitude(h, M)
if time:
    print(f'The balloon first touches ground at hour: {time}')
else:
    print("The balloon does not touch ground in the given time.")