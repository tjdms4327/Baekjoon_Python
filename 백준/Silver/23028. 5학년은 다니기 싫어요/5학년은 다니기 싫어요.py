import sys, math
input = sys.stdin.readline

n, a, b = map(int, input().split())
lectures = [list(map(int, input().split())) for _ in range(10)]

left = 8 - n
left_major = max(0, 66 - a)
left_total = max(0, 130 - b)

for i in range(left):
    x, y = lectures[i]
    
    take_major = min(x, math.ceil(left_major/3), 6)
    take_total = min(6, take_major+y)
    
    left_major -= take_major * 3
    left_total -= take_total * 3
    
if left_major <= 0 and left_total <= 0:
    print('Nice')
else:
    print('Nae ga wae')