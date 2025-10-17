# bronzeII_14623
import sys
input = sys.stdin.readline

bin1 = int(input(), 2)
bin2 = int(input(), 2)

result_bin = bin(bin1 * bin2)
print(str(result_bin)[2:])