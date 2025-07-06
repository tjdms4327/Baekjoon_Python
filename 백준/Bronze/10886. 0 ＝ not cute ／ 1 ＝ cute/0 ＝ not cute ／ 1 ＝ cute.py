n=int(input())
a=''
for j in range(n):
    i=input()
    if i=='0':
        a+='0'
    else:
        a+='1'

c0=a.count('0')
c1=a.count('1')
if c0>c1:
    print("Junhee is not cute!")
elif c0<c1:
    print("Junhee is cute!")
