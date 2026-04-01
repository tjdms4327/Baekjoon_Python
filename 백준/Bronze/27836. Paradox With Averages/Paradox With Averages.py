import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    input() # 테스트 케이스별 빈줄 처리
    
    n, m = map(int, input().split())
    c_iq = list(map(int, input().split()))
    e_iq = list(map(int, input().split()))
    
    c_sum = sum(c_iq)
    e_sum = sum(e_iq)
    
    count = 0
    for i in range(n):
        x = c_iq[i]
        if (c_sum > n * x) and (m * x > e_sum):
            count += 1
                
    print(count)