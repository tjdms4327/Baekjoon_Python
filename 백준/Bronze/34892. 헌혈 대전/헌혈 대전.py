import sys
input = sys.stdin.readline

n, a, b, c, d, e, f, g, h = map(int, input().split())

count = 0
xyz = []
for x in range(n+1):
    for y in range(0, n+1-x):
        z = n - x - y
        if a*x+b*y+c*z==d and e*x+f*y+g*z==h:
            count += 1
            xyz.append([x,y,z])
            
if count==1:
    print(0)
    for sol in xyz:
        print(*sol)
elif count > 1:
    print(1)
else:
    print(2)