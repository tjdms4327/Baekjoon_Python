from collections import Counter

a=list(input())
b=list(input())
counterA = Counter(a)
counterB = Counter(b)

intersection = counterA & counterB # 중복 원소 고려한 교집합
#print(list(intersection.elements()))
diff= (counterA-intersection)+(counterB-intersection) # 대칭차집합
print(sum(diff.values()))