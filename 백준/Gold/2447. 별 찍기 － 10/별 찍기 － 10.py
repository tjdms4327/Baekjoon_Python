import sys
input = sys.stdin.readline

def star(N):
    if N == 3:
        return ['***', '* *', '***']
    
    prev = star(N // 3)
    result = []
    
    for i in prev:
        result.append(i * 3) 
    for i in prev:
        result.append(i + ' '*(N//3) + i)  # 가운데 공백 블록
    for i in prev:
        result.append(i * 3)
        
    return result

N = int(input())
print('\n'.join(star(N)))