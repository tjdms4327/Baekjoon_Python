import sys
input=sys.stdin.readline

import math

# 삼각형 넓이는 세가지
# 1. 2L * L * (1/2) * sin60 
# 2. L * L * (1/2) * sin120
# 3. 2L * L * (1/2)
# 정육각형 나눴을 때 조합은 1+2, 2+3
# 첫번째 조합의 삼각형 최소넓이는 2
# 두번째 조합의 삼각형 최소넓이는 2
L=int(input().strip())
print(L * L * (1/2) * math.sin(math.pi*(120/180)))