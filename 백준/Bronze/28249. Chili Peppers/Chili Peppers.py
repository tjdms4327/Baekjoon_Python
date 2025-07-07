SHU={'Poblano':1500, 'Mirasol':6000, 'Serrano':15500, 'Cayenne':40000,
    'Thai':75000, 'Habanero':125000}

t=int(input())
total=0
for _ in range(t):
    pepper=input()
    total+=SHU.get(pepper)
print(total)