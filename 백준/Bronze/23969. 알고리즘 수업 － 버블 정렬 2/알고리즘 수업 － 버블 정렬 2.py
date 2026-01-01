import sys
input = sys.stdin.readline

'''
bubble_sort(A[1..N]) { # A[1..N]을 오름차순 정렬한다.
    for last <- N downto 2
        for i <- 1 to last - 1
            if (A[i] > A[i + 1]) then A[i] <-> A[i + 1]  # 원소 교환
}
'''

n, k = map(int, input().split())
A = list(map(int, input().split()))

for last in range(n, 1, -1):
    for i in range(0, last-1):
        if A[i] > A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
            k -= 1
            
            if k == 0:
                print(*A)
                sys.exit()

print(-1)
            