import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

cnt = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

result = []
for x, y in zip(a, b):
    i = (ord(x)-ord('A'))%26
    result.append(cnt[i])
    
    j = (ord(y)-ord('A'))%26
    result.append(cnt[j])
    
    
while len(result) > 2:
    result = [(result[i]+result[i+1])%10 for i in range(len(result)-1)]
    
print(f"{result[0]}{result[1]}")