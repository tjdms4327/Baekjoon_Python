t=int(input())
b=0;c=0;d=0;e=0
for i in range(t):
    a=int(input())
    b=a//25 ;a-=(b*25)
    c=a//10; a-=(c*10)
    d=a//5 ; a-=(d*5)
    e=a
    print(b,c,d,e)
    