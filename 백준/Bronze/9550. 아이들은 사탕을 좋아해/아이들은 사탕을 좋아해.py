t=int(input())
for _ in range(t):
  n,k=map(int, input().split())
  count_candy=list(map(int, input().split()))
  children=[i//k for i in count_candy]
  print(sum(children))