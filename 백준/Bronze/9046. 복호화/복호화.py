from collections import Counter

n=int(input())
for _ in range(n):
    s=input()

    filtered = [x for x in s if x.isalpha()]
    counter_s=Counter(filtered)
    #print(counter_s)
    max_cnt=max(counter_s.values())
    max_chr=[ch for ch, cnt in counter_s.items() if cnt==max_cnt]

    if len(max_chr)==1:
        print(max_chr[0])
    else:
        print('?')