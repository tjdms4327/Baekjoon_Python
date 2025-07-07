lv,a=input().split()
lv=int(lv)

if a=='miss':
    print(0)
elif a=='bad':
    print(lv*200)
elif a=='cool':
    print(lv*400) 
elif a=='great':
    print(lv*600)
else:
    print(lv*1000)