n=int(input())

final=[]
for i in range(1, n+1):
  cand = [n, i ]
  while len(cand)>=2 and (cand[-2]-cand[-1])>=0:
    cand.append(cand[-2]-cand[-1])
  if len(final)<=len(cand): final=cand
print(len(final))
print(*final)