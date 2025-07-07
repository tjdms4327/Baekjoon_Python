import sys
input=sys.stdin.readline

n=int(input())
for _ in range(n):
    item,price=map(int, input().split())
    charge=0
    if item==1:
        charge+=price
    else:
        charge+=item*(price-2)+2
    print(item, price)
    print(charge)