rods=list(map(int, input().split()))
rods.sort()

if min(rods)==max(rods):
    print(2)
elif rods[0]**2+rods[1]**2==rods[2]**2:
    print(1)
else:
    print(0)