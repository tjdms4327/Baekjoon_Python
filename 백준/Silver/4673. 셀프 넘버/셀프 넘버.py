n=[]
for i in range(1, 10001):
  n.append(i+sum(list(map(int, list(str(i))))))
  if i not in n:
    print(i)