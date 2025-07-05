def new_coke(e,f,c):
    bottle=e+f
    count=0
    while bottle>=c:
        count+=(bottle//c)
        bottle-=(bottle//c)*(c-1)
    print(count)

e,f,c=map(int, input().split())
new_coke(e,f,c)