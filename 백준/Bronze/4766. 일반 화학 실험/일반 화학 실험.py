temp=float(input())
while True:
  current=float(input())
  if current==999: break
  print(f"{current-temp:.2f}")
  temp=current