s=input()
length=len(s)

joi, ioi=0,0
for i in range(length-2):
    chunk=s[i:i+3]
    if chunk=='JOI':
        joi+=1
    elif chunk=='IOI':
        ioi+=1
print(joi, ioi, sep='\n')