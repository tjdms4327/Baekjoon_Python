x=int(input())
y=int(input())
sub=y-x

print("All positions change in year {}".format(x))
while True:
    if sub>=60:
        print("All positions change in year {}".format(x+60))
        x+=60
        sub-=60
    else:
        break