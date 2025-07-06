a=int(input())
b=int(input())

if a>=b:
    print('Congratulations, you are within the speed limit!')
else:
    d=b-a
    if d<=20:
        print('You are speeding and your fine is $100.')
    elif d<=30:
        print('You are speeding and your fine is $270.')
    else:
        print('You are speeding and your fine is $500.')