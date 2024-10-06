import sys
input = sys.stdin.readline

# 첫 번째 줄 처리
N, M = map(int, input().split())

# 두 번째 줄 처리
numbers = list(map(int, input().split()))

# 누적 합 배열
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + numbers[i - 1]

# 결과 계산
result = []
for _ in range(M):
    i, j = map(int, input().split())
    result.append(prefix_sum[j] - prefix_sum[i - 1])

# print("\n".join(map(str, result))) -> 메모리 사용 더 큼
for res in result:
    print(res)
