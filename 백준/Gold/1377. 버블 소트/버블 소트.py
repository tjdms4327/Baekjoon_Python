import sys
input = sys.stdin.readline

n = int(input())
A = [(int(input()), i) for i in range(n)]

max = 0
sorted_A = sorted(A)
for i in range(n):
    if max < sorted_A[i][1] - i: # 정렬 전 index - 정렬 후 index
        max = sorted_A[i][1] - i
print(max + 1) # swap이 일어나지 않는 반복문 한 번 더 실행되는 경우 감안