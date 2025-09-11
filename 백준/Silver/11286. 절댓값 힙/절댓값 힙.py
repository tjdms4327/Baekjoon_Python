import sys
input = sys.stdin.readline
print = sys.stdout.write
from queue import PriorityQueue

n = int(input()) # 연산 개수
myQueue = PriorityQueue()

for i in range(n):
    request = int(input())
    if request == 0:
        if myQueue.empty():
            print('0\n')
        else:
            temp = myQueue.get()
            print(str(temp[1])+'\n')
    else:
        myQueue.put((abs(request), request)) # 절대값 기준으로 정렬하고 같으면 음수 우선 정렬