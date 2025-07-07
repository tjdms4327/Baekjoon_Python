N=int(input())
K=input()

even=0
for i in range(N):
    num=int(K[i])
    if num%2==0:
        even+=1
odd=N-even

if even>odd:
    print(0)
elif even<odd:
    print(1)
else:
    print(-1)