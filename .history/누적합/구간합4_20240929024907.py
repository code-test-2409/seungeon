import sys
input = sys.stdin.read

data = input().split()

# 첫 번째 줄 처리
N = int(data[0])
M = int(data[1])

# 두 번째 줄 처리
num = list(map(int, data[2:N+2]))

# 누적 합 배열
sum = [0] * (N + 1)
for i in range(1, N + 1):
    sum[i] = sum[i - 1] + num[i - 1]

# 결과 계산
result = []
index = N + 2
for _ in range(M):
    i = int(data[index])
    j = int(data[index + 1])
    index += 2
    result.append(sum[j] - sum[i - 1])


print("\n".join(map(str, result)))
