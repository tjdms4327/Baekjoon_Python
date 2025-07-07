k=int(input())

charge=25+k*0.01
if charge<100:
    charge=100
elif charge>2000:
    charge=2000
print(f'{charge:.2f}')