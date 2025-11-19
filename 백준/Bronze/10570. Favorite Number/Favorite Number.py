# bronzeI_10570
import sys
input = sys.stdin.readline


for test in range(int(input())):
    count = [0] * 1001
    
    for _ in range(int(input())):
        s = int(input())
        count[s] += 1

    print(count.index(max(count)))