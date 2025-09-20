A = list(map(str, input().split("-")))

def mySum(i): 
    sum = 0
    temp = str(i).split("+")
    for i in temp:
        sum += int(i)
    return sum

answer = 0
for i in range(len(A)):
    temp = mySum(A[i])
    if i == 0:
        answer += temp # 맨 앞의 값 처리
    else:
        answer -= temp
print(answer)