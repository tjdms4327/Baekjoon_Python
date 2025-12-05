import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

time = (k+1) // n - 1
print(time)
