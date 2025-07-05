def price(parts):
  part_price= [350.34, 230.90, 190.55, 125.30, 180.90]
  tot=sum([part_price[i]*parts[i] for i in range(5)])
  return tot

n=int(input())
for i in range(n):
  parts=list(map(int, input().split()))
  print(f"${price(parts):.2f}")