n=int(input())

a_lst=list(input().split())
a=''.join(i for i in a_lst)
x=int(a)

b_lst=list(input().split())
b=''.join(i for i in b_lst)
y=int(b)

if x>=y:
    print(y)
else:
    print(x)