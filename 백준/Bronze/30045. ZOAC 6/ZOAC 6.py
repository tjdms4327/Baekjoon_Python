n=int(input())

OI=0
for _ in range(n):
    s=input()
    if '01' in s or 'OI' in s:
        OI+=1
        #print(s)
print(OI)