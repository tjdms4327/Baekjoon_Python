n = int(input())

for _ in range(n):
    s = input().strip()
    count_upper = sum('A' <= ch <= 'Z' for ch in s)
    count_lower = sum('a' <= ch <= 'z' for ch in s)
    
    if len(s) <= 10 and not s.isdigit() and count_upper <= count_lower:
        print(s)
