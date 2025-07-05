import sys
input = sys.stdin.readline

def count_common(N, A, M, B): # 한 테스트케이스에서 common element 수 세기
    i,j=0,0
    count=0
    while i<N and j<M:
        if A[i]==B[j]:
            count+=1
            i+=1
            j+=1
        elif A[i]<B[j]:
            i+=1
        else:
            j+=1
    return count

while True: # 여러개의 테스트 케이스
    N, M= map(int, input().strip().split())
    if N==0 and M==0: break # 입력 마지막 줄은 0 0
        
    N_list = [int(input().strip()) for _ in range(N)]
    M_list = [int(input().strip()) for _ in range(M)]
    result=count_common(N, N_list, M, M_list)
    print(result)