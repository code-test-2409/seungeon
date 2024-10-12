import sys
import heapq

input = sys.stdin.readline

n = int(input().strip())

# 수업 시간표 입력 받기
classes = [tuple(map(int, input().strip().split())) for _ in range(n)]

# 수업을 시작 시간 기준으로 정렬
classes.sort()

# 최소 힙을 사용하여 종료 시간을 관리
min_heap = []

# 첫 수업의 종료 시간을 힙에 추가
heapq.heappush(min_heap, classes[0][1])

for i in range(1, n):
    # 현재 수업의 시작 시간과 힙의 최소 종료 시간을 비교
    if classes[i][0] >= min_heap[0]:
        # 수업이 종료된 후 새로운 수업 시작 가능 (강의실 재사용)
        heapq.heappop(min_heap)
    # 새로운 수업의 종료 시간을 힙에 추가
    heapq.heappush(min_heap, classes[i][1])

# 힙의 크기가 필요한 강의실의 최소 개수
print(len(min_heap))