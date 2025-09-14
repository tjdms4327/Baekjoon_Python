import sys
input = sys.stdin.readline

result = 0

def merge_sort(s, e): # 병합 정렬
    global result
    if e - s < 1: return
    m = int(s + (e-s) / 2)
    merge_sort(s, m)
    merge_sort(m+1, e)
    for i in range(s, e+1):
        tmp[i] = A[i]
        
    k = s
    index1 = s
    index2 = m + 1
    while index1 <= m and index2 <= e: # 두 그룹 병합
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            result = result + index2 - k
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
    while index1 <= m: # 한쪽 그룹이 모두 선택된 후 남은 값 정리
        A[k] = tmp[index1]
        k+= 1
        index1 += 1
    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1

n = int(input())
A = list(map(int, input().split()))
A.insert(0,0)
tmp = [0] * int(n+1)
    
merge_sort(1, n)
print(result)