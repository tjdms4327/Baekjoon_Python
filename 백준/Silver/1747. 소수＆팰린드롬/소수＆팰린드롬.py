import math

n = int(input())
A = [0] * (10000001)
for i in range(2, len(A)):
    A[i] = i
# 에라토스테네스의 체
for i in range(2, int(math.sqrt(len(A)))+1):
    if A[i] == 0:
        continue
    for j in range(i+i, len(A), i):
        A[j] = 0

def isPalindrome(target):
    temp = list(str(target))
    s, e = 0, len(temp) - 1
    while s < e:
        if temp[s] != temp[e]:
            return False
        s += 1
        e -= 1
    return True

i = n
while True:
    if A[i] != 0:
        result = A[i]
        if isPalindrome(result):
            print(result)
            break
    i += 1