n=input()
length=len(n)
if length%3!=0:
    n='0'*(3-length%3)+n
    #print(n)

change={
    '000':'0', '001':'1', '010':'2', '011':'3', 
    '100':'4', '101':'5', '110':'6', '111':'7'
}
result=''
for i in range(0, length, 3):
    chunk=n[i:i+3]
    result+=change[chunk]
print(result)