def balance(S):
  stack=[]
  balance='yes'
  for i in S:
    if i in '([':
      stack.append(i)
    elif i == ')':
      if stack and stack[-1]=='(': stack.pop()
      else: balance='no' ; break
    elif i == ']':
      if stack and stack[-1]=='[': stack.pop()
      else: balance='no' ; break
  if stack: balance='no'
  return balance

while True:
  S=input()
  if S == ".": break
  else: print(balance(S))