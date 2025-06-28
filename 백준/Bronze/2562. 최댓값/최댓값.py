num=[]
for _ in range(9):
    num.append(int(input()))

max_val=max(num)
print(max_val, num.index(max_val)+1)