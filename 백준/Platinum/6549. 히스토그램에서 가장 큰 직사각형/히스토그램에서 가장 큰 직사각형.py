import sys
input=sys.stdin.readline

def maxsize():   #최대 크기의 직사각형 구하는 함수
    max_s=0   #최대 크기 
    stack=[]   #높이, 시작 인덱스 저장

    for i in range(n):
        idx=i   #현재 인덱스
        while stack and stack[-1][0]>=hs[i]:
            h, idx=stack.pop()
            size=h*(i-idx)   #현재 높이 h인 직사각형의 크기
            max_s=max(max_s, size)   #최대 크기 갱신
        stack.append([hs[i], idx])   #현재 높이와 시작인덱스 추가
    for h, left in stack:   #스택에 남아있는 직사각형 처리
        max_s=max(max_s, (n-left)*h)
    return max_s

result=[]
while True:
    n, *hs=map(int, input().split())
    if n==0:
        break
    result.append(maxsize())

print(*result, sep='\n')