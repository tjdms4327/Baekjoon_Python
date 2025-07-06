n=int(input())

cnt=0
for a in range(2, n+1, 2):
  for b in range(1, n-a+1):
    if n-a-b>=b+2: cnt+=1
print(cnt)