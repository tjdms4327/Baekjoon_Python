import sys
input = sys.stdin.readline

n = int(input()) # 수열 개수
A = list(map(int, input().split())) # 수열 리스트
answer = [0] * n
myStack = [] # 스택 선언 (인덱스 저장)

for i in range(n):
    while myStack and A[myStack[-1]] < A[i]:
        answer[myStack.pop()] = A[i]
    myStack.append(i)
while myStack:
    answer[myStack.pop()] = -1

for i in answer:
    sys.stdout.write(str(i)+' ')