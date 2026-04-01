import sys
input=sys.stdin.readline

A=input().strip()
B=input().strip()
# 열은 아스키코드 값으로 계산
move=[abs(ord(B[0])-ord(A[0])), abs(int(B[1])-int(A[1]))]
print(min(move), max(move))