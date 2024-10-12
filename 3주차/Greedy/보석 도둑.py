import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
gems = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

# 보석을 무게 기준으로 오름차순 정렬
gems.sort()
# 가방을 담을 수 있는 무게를 기준으로 오름차순 정렬
bags.sort()

result = 0
tmp = []

# 각 가방에 대해 가장 비싼 보석을 선택
for bag in bags:
    # 현재 가방에 담을 수 있는 모든 보석을 최대 힙에 추가
    while gems and gems[0][0] <= bag:
        heapq.heappush(tmp, -gems.pop(0)[1]) # 최대 힙 사용을 위해 음수로 저장
    
    # 가장 비싼 보석을 선택
    if tmp:
        result -= heapq.heappop(tmp)

print(result)