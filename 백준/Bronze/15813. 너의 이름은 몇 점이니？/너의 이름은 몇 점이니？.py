t=int(input())
s=input()
    
score=0
for i in s:
    score+=ord(i)-ord('A')+1
print(score)