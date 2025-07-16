def converge(lst):
    cnt=0
    while not(lst[0] == lst[1] == lst[2] == lst[3]):
        new_lst=[0]*4
        for i in range(3):
            new_lst[i]=(abs(lst[i]-lst[i+1]))
        new_lst[3] = abs(lst[3] - lst[0])    
        cnt+=1
        lst=new_lst
    return cnt

while True:
    nums=list(map(int, input().split()))
    if nums==[0,0,0,0]: break
    result=converge(nums)
    print(result)