n=int(input())

for i in range(1, 10):
    TF=False
    if n%i==0 and n//i<=9:
        TF=True
        break
if TF:
    print(1)
else:
    print(0)