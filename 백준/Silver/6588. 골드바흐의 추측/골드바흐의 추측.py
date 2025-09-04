import sys
input = sys.stdin.readline

MAX = 1000000
prime = [True] * (MAX+1)
prime[0] = prime[1] = False

# 에라토스테네스의 체
for i in range(2, int(MAX**0.5)+1):
    if prime[i]:
        for j in range(i*i, MAX+1, i):
            prime[j] = False
    
while True:
    n = int(input())
    if n == 0: break

    for i in range(3, n//2 + 1, 2):  # 홀수 소수 a
        if prime[i] and prime[n-i]:
            print(f'{n} = {i} + {n-i}')
            break
    else:
        print("Goldbach's conjecture is wrong.")