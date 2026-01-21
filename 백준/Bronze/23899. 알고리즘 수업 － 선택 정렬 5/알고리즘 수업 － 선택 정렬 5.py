import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if A == B:
        print(1)
        sys.exit()

'''
selection_sort(A[1..N]) { # A[1..N]을 오름차순 정렬한다.
    for last <- N downto 2 {
        A[1..last]중 가장 큰 수 A[i]를 찾는다
        if (last != i) then A[last] <-> A[i]  # last와 i가 서로 다르면 A[last]와 A[i]를 교환
    }
}
'''

for last in range(n-1, 0, -1):
    max_idx = max(range(last+1), key=lambda i: A[i])
    if (last != max_idx):
        A[last], A[max_idx] = A[max_idx], A[last]
    if A == B:
        print(1)
        sys.exit()
print(0)