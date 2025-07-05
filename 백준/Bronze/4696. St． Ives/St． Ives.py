n=float(input())
while n != 0:
    a=1+n+n**2+n**3+n**4
    # 2 decimal points
    #print(round(a,2))
    print("{:.2f}".format(a))
    n=float(input())