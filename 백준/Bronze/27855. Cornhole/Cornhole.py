one3, one1=map(int, input().split())
two3, two1=map(int, input().split())

one=3*one3+one1
two=3*two3+two1
diff=abs(one-two)

if diff==0:
    print('NO SCORE')
elif one>two: 
   print(1, diff)
else:
   print(2, diff)