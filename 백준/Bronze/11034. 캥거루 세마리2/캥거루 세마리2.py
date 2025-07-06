while True:
  try:
    a,b,c=map(int, input().split())
    max_length=max(b-a, c-b)
    print(max_length-1)
  except EOFError: break