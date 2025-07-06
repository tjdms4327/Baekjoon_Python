by, bm, bd = map(int, input().split())
y, m, d = map(int, input().split())

year=y-by
#만 나이
if (m<bm) or ((m==bm) and (d<bd)):
    print(year-1)
else:
    print(year)
#세는 나이
print(year+1)
#연 나이
print(year)