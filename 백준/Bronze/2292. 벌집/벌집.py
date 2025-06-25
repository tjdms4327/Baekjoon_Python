n=int(input())

room=1
now=1
temp=1
while n>now:
    now+=6*temp
    temp+=1
    room+=1
print(room)