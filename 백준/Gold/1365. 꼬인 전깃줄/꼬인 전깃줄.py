import sys
input = sys.stdin.readline
import bisect

n = int(input())
line = list(map(int, input().split()))

arr = [] # 길이 i 증가수열의 최소 끝값
for x in line:
    idx = bisect.bisect_left(arr, x)
    if idx == len(arr): # 맨 뒤에 붙으면
        arr.append(x)
    else:
        arr[idx] = x
        
print(n - len(arr))