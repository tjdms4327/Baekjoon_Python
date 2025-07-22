n=int(input())
s=input()

b=s.count('bigdata')
s=n-b
if b>s:
    print('bigdata?')
elif b==s:
    print("bigdata? security!")
else:
    print('security!')