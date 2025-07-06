l=int(input())
s=input()

temp=31
tot=0
for i in range(l):
    c=ord(s[i])-96
    tot+=(c*(temp**i))
print(tot%1234567891)