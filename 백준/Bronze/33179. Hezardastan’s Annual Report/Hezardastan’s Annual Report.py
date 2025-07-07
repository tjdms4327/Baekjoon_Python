import sys
input=sys.stdin.readline

n=int(input().strip())
pages=list(map(int, input().strip().split()))

sheets=0
for i in pages:
    if i%2!=0: sheets+=(i//2 + 1) # 홀수 페이지면 마지막에 blank page 추가
    else: sheets+=(i//2)
print(sheets)