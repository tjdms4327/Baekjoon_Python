a=input()
b=len(a)/2

if b-int(b)==0 :
    c=a[int(b):len(a)]
    print(int(a[0:int(b)]==c[::-1]))
else:
    c=a[int(b+1):len(a)]
    print(int(a[0:int(b)]==c[::-1]))