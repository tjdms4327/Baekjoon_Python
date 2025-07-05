import sys
input=sys.stdin.readline

def diff_chars(s1, s2):
    return sum(1 for a, b in zip(s1, s2) if a!=b)

t=int(input())
for _ in range(t):
    s1=input()
    s2=input()
    diff=diff_chars(s1,s2)
    print(f'Hamming distance is {diff}.')