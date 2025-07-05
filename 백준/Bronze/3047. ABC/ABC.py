num=list(map(int, input().split()))
num.sort()

order=list(input())
idx={'A':0, 'B':1, 'C':2}

for i in range(3):
    print(num[idx[order[i]]], end=' ')