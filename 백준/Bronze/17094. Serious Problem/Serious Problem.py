l=int(input())
s=list(input())
e=s.count('e')
if e<l-e:
    print(2)
elif 2*e==l:
    print ("yee")
else:
    print("e")