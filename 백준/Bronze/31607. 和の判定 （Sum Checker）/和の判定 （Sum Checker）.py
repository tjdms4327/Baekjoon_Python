A=int(input())
B=int(input())
C=int(input())

num=[A,B,C]
num.sort()
if (num[0]+num[1])==num[2]:
    print(1)
else:
    print(0)