t=int(input())
for _ in range(t):
  input()
  r,c=map(int, input().split())

  candy=[]
  for i in range(r):
    candy.append(input())

  cnt=0
  for i in range(r):
    for j in range(c):
      if j<=c-3 and candy[i][j:j+3]=='>o<': cnt+=1
      elif i<=r-3 and (candy[i][j] == 'v' and candy[i+1][j] == 'o' and candy[i+2][j] == '^'): cnt+=1
  print(cnt)