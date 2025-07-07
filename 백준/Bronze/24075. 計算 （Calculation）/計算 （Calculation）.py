a,b=map(int, input().split())

sum,subtract=a+b, a-b
print(max(sum, subtract))
print(min(sum, subtract))