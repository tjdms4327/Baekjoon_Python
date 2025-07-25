s=input()
filtered=''.join(i for i in s if i.isalpha())
k=input()

if k in filtered:
    print(1)
else: print(0)