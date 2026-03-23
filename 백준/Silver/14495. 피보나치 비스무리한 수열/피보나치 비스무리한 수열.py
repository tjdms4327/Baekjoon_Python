import sys
input = sys.stdin.readline

n = int(input())

fibo = [1] * (n+1) # fibo[0]은 무시
for i in range(4, n+1):
    fibo[i]= fibo[i-1] + fibo[i-3]
    
print(fibo[n])