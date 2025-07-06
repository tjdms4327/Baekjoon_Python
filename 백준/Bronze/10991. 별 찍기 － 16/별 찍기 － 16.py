n=int(input())
for i in range(1,n+1):
    a=' '.join('*'*(i))
    a=(' '*(n-i)+a)
    print(a)