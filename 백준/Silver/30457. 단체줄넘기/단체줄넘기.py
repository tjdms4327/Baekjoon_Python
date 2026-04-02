import sys
input = sys.stdin.readline

n = int(input())
H = list(map(int, input().split()))
H.sort()

left, right = [H[0]], []
for h in H[1:]:
    if h > left[-1]:
        left.append(h)
    else:
        if not right:
            right.append(h)
        else:
            if h > right[-1]:
                right.append(h)
                
print(len(left+right))
