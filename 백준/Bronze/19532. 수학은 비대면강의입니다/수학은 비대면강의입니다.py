a,b,c,d,e,f=map(int, input().split())

down=a*e - b*d
print((c*e-f*b)//down, (-c*d+f*a)//down)