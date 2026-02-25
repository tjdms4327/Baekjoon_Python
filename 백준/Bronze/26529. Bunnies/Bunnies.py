import sys
input = sys.stdin.readline

fibo = [0]*(46)
fibo[0] = fibo[1] = 1
for i in range(2, 46):
    fibo[i] = fibo[i-1] + fibo[i-2]

n = int(input())
for _ in range(n):
    x = int(input())
    print(fibo[x])