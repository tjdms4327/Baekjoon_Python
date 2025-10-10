# bronzeIII_10395
import sys
input = sys.stdin.readline

x = list(input().split())
y = list(input().split())

for i in range(5):
    if x[i] == y[i]:
        print('N')
        exit()
print('Y')