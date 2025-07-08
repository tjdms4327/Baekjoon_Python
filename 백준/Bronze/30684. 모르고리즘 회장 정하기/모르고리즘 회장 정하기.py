import sys
input=sys.stdin.readline

n=int(input().strip()) 
cand='ZZZ' # 세글자 이름은 무조건 존재하므로 비교 가능
for _ in range(n):
    s=input().strip()
    if len(s)==3 and s<cand: # 문자열 비교는 사전순
        cand=s
print(cand)