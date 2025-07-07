a=['Never gonna give you up','Never gonna let you down','Never gonna run around and desert you','Never gonna make you cry','Never gonna say goodbye','Never gonna tell a lie and hurt you','Never gonna stop']
b=0
for i in range(int(input())):
    s=input()
    if s not in a:
        b+=1
if b !=0:
    print('Yes')
else:
    print('No')