import sys
input=sys.stdin.readline

FBI=[]
for i in range(1, 5+1):
    name=input()
    if 'FBI' in name:
        FBI.append(i)
if FBI==[]:
    print("HE GOT AWAY!")
else:
    print(*FBI)