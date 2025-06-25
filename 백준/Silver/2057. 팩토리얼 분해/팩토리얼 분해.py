n=int(input())

def factorial(n):
  f=[]
  for i in range(n+1):
    num=1
    for j in range(1,i+1):
      num*=j
    if num>n: break
    f.append(num)
  return f

from itertools import combinations
def subset(list, target):
  for s in range(1, len(list) + 1):
    for subset in combinations(list, s):
      if sum(subset) == target:
        return "YES"
  return "NO"

print(subset(factorial(n), n))  