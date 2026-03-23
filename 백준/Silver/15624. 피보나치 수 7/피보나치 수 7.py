import sys
input = sys.stdin.readline

n = int(input())
if n == 0:
    print(0)
    sys.exit()

fibo = [0] * (n+1) 
fibo[1] = 1
for i in range(2, n+1):
    fibo[i] = (fibo[i-1] + fibo[i-2])%1000000007
    
print(fibo[n])