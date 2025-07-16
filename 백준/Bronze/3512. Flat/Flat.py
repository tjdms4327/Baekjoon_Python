tot_area, bed_area, bal_area=0,0,0

n,c=map(int, input().split())
for _ in range(n):
    a, t=input().split()
    a=int(a)
    tot_area+=a
    if t=='bedroom': bed_area+=a
    elif t=='balcony': bal_area+=a
print(tot_area)
print(bed_area)
print((tot_area-bal_area/2)*c)