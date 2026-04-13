import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
cnts = list(map(int, input().split()))

def dfs(index, current):
    global best_min, best_max
    
    if index == n:
        best_min = min(best_min, current)
        best_max = max(best_max, current)
        return
    
    next_num = A[index]
    for i in range(4):
        if cnts[i] > 0:
            cnts[i] -= 1

            if i == 0:
                next_val = current + next_num
            elif i == 1:
                next_val = current - next_num
            elif i == 2:
                next_val = current * next_num
            else:
                if current < 0:
                    next_val = -(-current // next_num)
                else:
                    next_val = current // next_num
                
            dfs(index+1, next_val)
            cnts[i] += 1
            
            
best_min = int(1e9)
best_max = -int(1e9)
dfs(1, A[0])

print(best_max)
print(best_min)