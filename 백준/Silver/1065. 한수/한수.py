N=int(input())

count=0
for i in range(1, N+1):
  nums=list(map(int, list(str(i))))
  if len(nums)<=2: count+=1
  elif sum(nums)==3*nums[1]: count+=1
print(count)