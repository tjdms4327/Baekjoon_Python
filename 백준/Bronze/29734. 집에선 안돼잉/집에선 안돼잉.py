# bronzeII_29734
import sys
input = sys.stdin.readline

n, m = map(int, input().split())  
t, s = map(int, input().split())  

zip_time = n + (n - 1) // 8 * s  
dok_time = t + m + (m - 1) // 8 * (2 * t + s)

if zip_time < dok_time:
    print("Zip")
else:
    print("Dok")
print(min(zip_time, dok_time))
