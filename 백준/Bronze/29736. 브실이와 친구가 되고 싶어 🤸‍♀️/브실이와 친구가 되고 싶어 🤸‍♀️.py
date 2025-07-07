A, B = map(int, input().split())
K, X = map(int, input().split())

left = max(A, K - X)
right = min(B, K + X)

friend = max(0, right - left + 1)
if friend > 0:
    print(friend)
else:
    print("IMPOSSIBLE")
