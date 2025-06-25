n=int(input())
num=list(map(int, input().split()))

young0, min0=[],[]
for i in range(n):
    young0.append((int(num[i]/30)+1)*10)
    min0.append((int(num[i]/60)+1)*15)
young, min=sum(young0), sum(min0)
#print(young, min)

if young>min:
    print('M', min)
elif young ==min:
    print('Y M', young)
else:
    print('Y', young)