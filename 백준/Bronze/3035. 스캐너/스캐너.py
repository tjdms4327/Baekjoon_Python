r,c,zr,zc=map(int, input().split())
for i in range(r):
    ss=input()
    for z in range(zr):
        print(''.join([s * zc for s in ss]))
    