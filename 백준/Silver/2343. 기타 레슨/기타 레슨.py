n, m = map(int, input().split())
A = list(map(int, input().split()))
start, end = 0, 0

for i in A:
    if start < i:
        start = i # 레슨 최댓값을 인덱스로 저장
    end += i # 모든 레슨의 총합을 종료 인덱스로 저장

while start <= end:
    middle = int((start + end) / 2)
    sum = 0
    count = 0
    for i in range(n): # 중앙값으로 모든 레슨을 저장할 수 있는지 확인
        if sum + A[i] > middle:
            count += 1
            sum = 0
        sum += A[i]
        
    if sum != 0:
        count += 1
        
    if count > m:
        start = middle + 1
    else:
        end = middle - 1
        
print(start)