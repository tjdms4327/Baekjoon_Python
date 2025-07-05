while True:
  try:
    n,m=map(int, input().split())

    cnt=0
    for i in range(n,m+1):
      num=list(str(i))
      if len(set(num))==len(num): cnt+=1
    print(cnt)
  except EOFError: break