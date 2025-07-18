n=int(input())
if n<100:
    print(99)
elif n%100>=49:
    print((n//100)*100+99)
else:
    print((n//100-1)*100+99)