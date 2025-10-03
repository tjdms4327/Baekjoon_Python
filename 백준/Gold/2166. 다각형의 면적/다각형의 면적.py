# goldV_2166
import sys
input = sys.stdin.readline

n = int(input())
x, y =[], []
for i in range(n):
    tempX, tempY = map(int, input().split())
    x.append(tempX)
    y.append(tempY)
x.append(x[0])
y.append(y[0])

result = 0
for i in range(n):
    result += (x[i]*y[i+1]) - (x[i+1]*y[i])
print(round(abs(result/2), 1))