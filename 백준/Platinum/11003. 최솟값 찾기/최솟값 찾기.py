import sys
input = sys.stdin.readline

from collections import deque

n, l = map(int, input().split()) # 수의 개수, 슬라이딩 윈도우 크기
A = list(map(int, input().split())) # n개의 수

mydeque =deque()
for i in range(n):
    while mydeque and mydeque[-1][0] > A[i]:
        mydeque.pop()
    mydeque.append((A[i], i)) #(값, 인덱스) 추가
    if mydeque[0][1] <= i - l: # 슬라이딩 범위에서 벗어나면
        mydeque.popleft() # 맨 앞 값 제거
    print(mydeque[0][0], end =' ')