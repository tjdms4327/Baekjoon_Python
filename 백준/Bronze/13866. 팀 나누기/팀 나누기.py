a,b,c,d=map(int,input().split())
m=[abs(a+b-(c+d)),abs(a+c-(b+d)),abs(a+d-(b+c))]

print(min(m))