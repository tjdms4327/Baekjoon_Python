N=int(input())
K=int(input())

primes = [0] * (N + 1)
for i in range(2, N+1):
  if primes[i]==0:
    for j in range(i, N+1, i):
      primes[j]=i

cnt=0
for i in range(1, N+1):
  if i==1 and i<=K: cnt+=1
  elif primes[i]<=K:cnt+=1
print(cnt)