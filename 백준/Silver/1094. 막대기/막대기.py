x=int(input())
rod=64
num=0
while x>0:
    if x>=rod:
        x-=rod
        num+=1
    else:
        rod=rod//2
print(num)