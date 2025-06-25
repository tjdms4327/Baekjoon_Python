import sys
input=sys.stdin.readline
import heapq

n=int(input())
card=[int(input()) for _ in range(n)]

heapq.heapify(card) #최소 힙으로 변환
compare=0
while len(card)>1:
    a=heapq.heappop(card) #최소 힙에서 가장 작은 원소 두 원소 꺼내 합치기
    b=heapq.heappop(card)
    compare+=(a+b)
    heapq.heappush(card, a+b) #힙에 원소 추가
print(compare)