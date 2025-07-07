m1,m2,m3=map(int,input().split())
m=m1*3+m2*20+m3*120
m12,m22,m32=map(int,input().split())
m0=m12*3+m22*20+m32*120

if m>m0:
    print('Max')
elif m<m0:
    print('Mel')
else:
    print('Draw')