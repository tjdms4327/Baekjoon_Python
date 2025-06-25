N = int(input())
result=0
 
for i in range(1, N):        
    nums = list(map(int, str(i)))  
    tot = i + sum(nums)              
    if(tot == N):         
        result=i
        break
print(result)