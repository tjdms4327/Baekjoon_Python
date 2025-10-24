# bronzeII_2684
import sys
input = sys.stdin.readline

coin3_pattern = ['TTT', 'TTH', 'THT', 'THH', 
                 'HTT', 'HTH', 'HHT', 'HHH']

n = int(input())
for _ in range(n):
    s = input().strip()
    
    result = [0]*8
    for i in range(len(s)-2):
        triple = s[i:i+3]
        if triple in coin3_pattern:
            idx = coin3_pattern.index(triple)
            result[idx] += 1
    print(*result)