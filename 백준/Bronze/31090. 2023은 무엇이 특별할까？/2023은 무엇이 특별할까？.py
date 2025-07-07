t=int(input())

for _ in range(t):
    a=input()
    b=int(a) ; c=int(a[-2:])
    if (b+1)%c==0:
        print('Good')
    else:
        print('Bye')