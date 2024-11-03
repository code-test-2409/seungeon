import sys
import heapq

input = sys.stdin.read
data = input().split()

n = int(data[0])
index = 1

# 사람들의 집과 사무실 위치를 저장할 리스트
people = []

for i in range(n):
    hi = int(data[index])
    oi = int(data[index + 1])
    index += 2
    if hi > oi:
        hi, oi = oi, hi
    people.append((hi, oi))

# 철로의 길이
d = int(data[index])

# 사무실 위치를 기준으로 정렬
people.sort(key=lambda x: x[1])

# 우선순위 큐
min_heap = []
max_count = 0

for hi, oi in people:
    # 현재 구간에 포함되는 사람들을 힙에 추가
    if oi - hi <= d:
        heapq.heappush(min_heap, hi)
    
    # 구간에서 벗어난 사람들은 힙에서 제거
    while min_heap and min_heap[0] < oi - d:
        heapq.heappop(min_heap)
    
    # 현재 구간에 포함된 사람들의 수를 최대값으로 갱신
    max_count = max(max_count, len(min_heap))

print(max_count)