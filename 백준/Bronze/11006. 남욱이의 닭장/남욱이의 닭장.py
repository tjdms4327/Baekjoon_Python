t=int(input())
for _ in range(t):
  n,m=map(int, input().split())
  lost_legs=2*m-n
  print(lost_legs, m-lost_legs)