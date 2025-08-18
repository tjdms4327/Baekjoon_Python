nums=list(map(int, input().split()))

pos_num=sum(x>0 for x in nums)
print(pos_num)