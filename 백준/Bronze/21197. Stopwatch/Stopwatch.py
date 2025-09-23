# bronzeIII_21197.py
import sys
input = sys.stdin.readline

n = int(input())
time = [int(input()) for _ in range(n)]

if n % 2 == 1:
    print('still running')
    sys.exit()
    
count = 0
for i in range(0, n, 2):
    count += time[i+1] - time[i]
print(count)