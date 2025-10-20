s = input().strip()

A = s.count('A')
B = s.count('B')
C = s.count('C')
D = s.count('D')
F = s.count('F')
plus = s.count('+')

sum_class = A + B + C + D + F
sum_score = 4 * A + 3 * B + 2 * C + D + 0.5 * plus
print(sum_score / sum_class)