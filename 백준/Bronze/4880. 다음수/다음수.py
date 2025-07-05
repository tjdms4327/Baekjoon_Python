while True:
  a,b,c=map(int, input().split())
  if a==0 and b==0 and c==0: break
  elif a+c==2*b: print('AP', c+(c-b))
  elif a*c==b*b: print('GP', c*(c//b))