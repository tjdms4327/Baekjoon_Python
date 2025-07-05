import sys
input = sys.stdin.readline

def wait_min(N, T):
    min_time=float('inf') # 양의 무한대로 초기화
    for i in range(N):
        Si, Ii, Ci=map(int, input().strip().split()) 
        # 역에 도착한 시간 T보다 크거나 같을 때만 저장
        bus=[Si+Ii*j for j in range(Ci) if Si+Ii*j>=T]
        if not bus: # 빈 리스트면(역에 도착하기 전에 버스가 다 떠났으면)
            continue
        cand=min(bus)-T
        if cand<min_time: 
            min_time=cand # 최소시간 갱신
    if min_time==float('inf'):
        return -1 # 버스가 없다.
    return min_time

N,T=map(int, input().strip().split())
result=wait_min(N, T)
print(result)