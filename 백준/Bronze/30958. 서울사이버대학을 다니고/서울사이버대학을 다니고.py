from collections import Counter

n=int(input())
s=input()

s=''.join(i for i in s if i.isalpha()) # 알파벳만 남김
counter=Counter(s.upper())
print(max(counter.values()))