n=0
for _ in range(6):
    a=input()
    if a=='W':
        n+=1
if n>=5:
    print(1)
elif n>=3:
    print(2)
elif n>=1:
    print(3)
else:
    print(-1)