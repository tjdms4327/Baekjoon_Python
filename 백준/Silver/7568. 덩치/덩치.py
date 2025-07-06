N=int(input())
xy=[tuple(map(int, input().split()))for _ in range(N)]

for i in xy:
  rank=1
  for j in xy:
    if i==j: continue
    elif i[0]<j[0] and i[1]<j[1]:
      rank+=1
  print(rank, end=' ')