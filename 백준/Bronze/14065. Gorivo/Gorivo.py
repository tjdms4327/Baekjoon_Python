mile_gallon=float(input())
km_l=mile_gallon*(1/3.785411784)*(1.609344)

print(f'{1/km_l*100:.6f}')