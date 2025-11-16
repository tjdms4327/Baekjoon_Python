# bronzeI_27494
import sys
input = sys.stdin.readline

n = int(input())


if n < 2023:
    print(0)
    sys.exit()
    
count = 0    
for num in range(2023, n+1):
    x = str(num)
    if not {'2', '3', '0'}.issubset(set(x)):
        continue
    
    tmp = []
    for i in x:
        if i =='2' and len(tmp) in [0, 2]:
            tmp.append(i)
        elif i == '0' and len(tmp)==1:
            tmp.append(i)
        elif i=='3' and len(tmp)==3:
            count += 1
            break
print(count)
        