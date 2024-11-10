import heapq

def minimum_black_to_white(n, grid):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    # 비용 배열 초기화
    costs = [[float('inf')] * n for _ in range(n)]
    costs[0][0] = 0
    
    # 우선순위 큐 초기화
    priority_queue = []
    heapq.heappush(priority_queue, (0, 0, 0))  # (변환한 검은 방 수, x, y)
    
    while priority_queue:
        cost, x, y = heapq.heappop(priority_queue)
        
        # 끝방에 도달하면 현재 비용 반환
        if x == n - 1 and y == n - 1:
            return cost
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                # 다음 방이 흰 방이면 비용 추가 없이 이동
                new_cost = cost + (1 if grid[nx][ny] == 0 else 0)
                
                # 더 적은 비용으로 방에 도달할 수 있는 경우
                if new_cost < costs[nx][ny]:
                    costs[nx][ny] = new_cost
                    heapq.heappush(priority_queue, (new_cost, nx, ny))
    
    return -1  # 만약 끝 방에 도달할 수 없는 경우

# 입력 받기
n = int(input().strip())
grid = [list(map(int, input().strip())) for _ in range(n)]

# 결과 출력
print(minimum_black_to_white(n, grid))