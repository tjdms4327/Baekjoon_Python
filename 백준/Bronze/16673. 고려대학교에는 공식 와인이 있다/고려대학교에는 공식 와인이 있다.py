def equation(c, K, P):
  return K*c+P*c*c

def year_c(C,K,P):
  tot=0
  for i in range(1, C+1):
    tot+=equation(i, K, P)
  return tot

C, K, P=map(int, input().split())
print(year_c(C, K, P))