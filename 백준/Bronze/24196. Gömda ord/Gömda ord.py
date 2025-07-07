s=input()

i=0
new=s[i]
while i<len(s)-1:
    i+=ord(new[-1])-64
    new+=s[i]
print(new)