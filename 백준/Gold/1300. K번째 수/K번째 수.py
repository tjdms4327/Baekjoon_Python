n = int(input())
k = int(input())

start, end = 1, k
answer = 0
while start <= end:
    middle = int((start+end) / 2)
    cnt = 0 # 중앙값보다 작은 수의 개수
    # 중앙값보다 작은 수 계산
    for i in range(1, n+1):
        cnt += min(int(middle / i), n)
    if cnt < k:
        start = middle + 1
    else:
        answer = middle
        end = middle - 1
print(answer)