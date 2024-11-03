import math
import sys

input = sys.stdin.read
data = input().split()

T = int(data[0])
index = 1

results = []

for _ in range(T):
    N = int(data[index])
    M = int(data[index + 1])
    index += 2

    # 조합 계산
    result = math.comb(M, N)
    results.append(result)

for result in results:
    print(result)