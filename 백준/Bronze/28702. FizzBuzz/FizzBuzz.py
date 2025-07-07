def FizzBuzz(i):
    if i%15==0:
        return 'FizzBuzz'
    elif i%3==0:
        return 'Fizz'
    elif i%5==0:
        return 'Buzz'
    else:
        return i

a=input()
b=input()
c=input()

if a.isdigit():
    x=int(a)+3
elif b.isdigit():
    x=int(b)+2
elif c.isdigit():
    x=int(c)+1
print(FizzBuzz(x))