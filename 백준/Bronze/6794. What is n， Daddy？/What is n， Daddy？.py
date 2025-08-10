n=int(input())

left, right, answer=0,0,0
while left<=5 and right<=5:
    if left+right==n and left>=right:
        answer+=1
        right+=1
        left=0
        
    if left==5:
        right+=1
    else:
        left+=1
print(answer)