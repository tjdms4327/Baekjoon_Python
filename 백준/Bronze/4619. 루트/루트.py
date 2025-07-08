import sys
input=sys.stdin.readline

while True:
  b, n=map(int, input().strip().split())
  if b+n==0: break # b와 n은 모두 1 이상
      
  ans, a=-1, 1
  min_diff=float('inf')
  while True:
      power=a**n
      diff=abs(power-b)
      if diff<min_diff:
          min_diff=diff
          ans=a
      else: break
      a+=1
  print(ans)