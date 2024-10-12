from collections import deque

def bfs(n, m, graph):
    # 이동 방향 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 방문 기록 (방문 여부, 벽 부수기 여부)
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    
    # 시작점 초기화
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1
    
    while queue:
        x, y, wall_break = queue.popleft()
        
        # 목적지 도착
        if x == n - 1 and y == m - 1:
            return visited[x][y][wall_break]
        
        # 네 방향 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m:
                # 벽이 없는 경우
                if graph[nx][ny] == 0 and visited[nx][ny][wall_break] == 0:
                    visited[nx][ny][wall_break] = visited[x][y][wall_break] + 1
                    queue.append((nx, ny, wall_break))
                
                # 벽이 있는 경우 (벽을 아직 부수지 않았고, 벽을 부수는 경우)
                if graph[nx][ny] == 1 and wall_break == 0 and visited[nx][ny][1] == 0:
                    visited[nx][ny][1] = visited[x][y][wall_break] + 1
                    queue.append((nx, ny, 1))
    
    # 도달 불가능한 경우
    return -1

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

result = bfs(n, m, graph)
print(result)