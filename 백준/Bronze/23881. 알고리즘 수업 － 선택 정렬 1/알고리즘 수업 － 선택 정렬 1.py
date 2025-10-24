# bronzeII_23881
import sys

N, K = list(map(int, sys.stdin.readline().rsplit()))
lst = list(map(int, sys.stdin.readline().rsplit()))

def selection_sort(N):
    cnt = 0    
    for i in range(N-1, 0, -1):
        last = i
        for j in range(i-1, -1, -1):
            if (lst[j] > lst[last]):
                last = j        
        if last != i:
            lst[i], lst[last] = lst[last], lst[i]
            cnt += 1
        if (cnt == K):            
            return (print(lst[last], lst[i]))
    return(print(-1))

selection_sort(N)
