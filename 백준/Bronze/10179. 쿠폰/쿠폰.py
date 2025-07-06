n=int(input())
for _ in range(n):
  price=float(input())
  discount_price=price*0.8
  print(f'${discount_price:.2f}')