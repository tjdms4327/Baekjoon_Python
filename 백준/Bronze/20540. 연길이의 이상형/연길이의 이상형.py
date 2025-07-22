infp=['I', 'N', 'F', 'P']
estj=['E', 'S', 'T', 'J']

name=input()
for i in range(4):
    cur=name[i]
    if cur in infp:
        print(estj[i], end='')
    else:
        print(infp[i], end='')