N, S=map(int, input().split())

cows=[int(input()) for _ in range(N)]
cows.sort()

fit=0
left, right=0, N-1
while left<right:
  if cows[left]+cows[right]<=S: 
    fit+=right-left
    left+=1
  else: right-=1

print(fit)