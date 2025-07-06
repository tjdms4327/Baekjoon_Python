a=input()
tot=10
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        tot+=5
    else:
        tot+=10
print(tot)