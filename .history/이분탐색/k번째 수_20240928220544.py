# https://www.acmicpc.net/problem/1300

def count(x, N):
    count = 0
    for i in range(1, N + 1):
        count += min(x // i, N)  # i * j ≤ x인 j의 최대 값은 min(x // i, N)
    return count

def find_k(N, k):
    left, right = 1, N * N
    while left < right:
        mid = (left + right) // 2
        if count(mid, N) < k:
            left = mid + 1  # mid보다 큰 값에서 k번째를 찾아야 함
        else:
            right = mid  # mid가 k번째보다 작거나 같으면 left에서 찾기
    return left

N = int(input())
k = int(input())

# k번째 원소 찾기
result = find_k(N, k)
print(result)