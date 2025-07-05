while True:
  a, b = input().split()
  if a=='0' and b=='0': break

  length=max(len(a), len(b))
  a=a.zfill(length) ; b=b.zfill(length)
  carry, carry_count=0,0
  for i in range(length-1, -1, -1):
    if (int(a[i])+int(b[i])+carry)>=10 : carry_count+=1 ; carry=1
    else: carry=0
  print(carry_count)