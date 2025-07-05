import sys
input = sys.stdin.readline

def find_common(note2, note1):
    note1_set = set(note1)  # 검색 효율 위해 집합으로 변환
    result = []
    for elem in note2:
        if elem in note1_set:
            result.append(1)
        else:
            result.append(0)
    return result

T=int(input().strip())
for i in range(T):
    N=int(input().strip())
    note1=list(map(int, input().strip().split()))
    M=int(input().strip())
    note2=list(map(int, input().strip().split()))
    result=find_common(note2, note1)
    print(*result, sep='\n')

