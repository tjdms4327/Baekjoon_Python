moose=list(map(int, input().split()))

if moose[0]==0 and moose[1]==0:
    print("Not a moose")
elif moose[0]==moose[1]:
    print('Even', moose[0]+moose[1])
else:
    print('Odd', max(moose)*2)