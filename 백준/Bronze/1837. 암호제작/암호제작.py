P, K=map(int, input().split())

is_prime=[1]*K
is_prime[0]=is_prime[1]=0
for i in range(2, int(K**0.5)+1):
    if is_prime[i]:
        for j in range(i*i, K, i): is_prime[j]=False
    
primes=[i for i, val in enumerate(is_prime) if val]
for prime in primes:
    if P%prime==0: print('BAD', prime); break
else: print('GOOD')