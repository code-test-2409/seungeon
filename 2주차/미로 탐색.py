from collections import deque

def bfs_maze(maze, n, m):
    # 이동할 네 방향 정의 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # BFS 큐 생성 및 초기 위치
    queue = deque([(0, 0)])
    maze[0][0] = 1  # 시작 위치의 칸 수를 1로 설정
    
    while queue:
        x, y = queue.popleft()
        
        # 현재 위치가 목표 위치이면 그 위치의 값을 반환
        if x == n - 1 and y == m - 1:
            return maze[x][y]
        
        # 네 방향으로 이동
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 미로를 벗어나지 않고, 이동할 수 있는 칸이면
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                # 새로운 위치로 이동한 칸 수를 현재 칸 수 + 1로 설정
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    
    return -1  # 도달할 수 없는 경우

# 입력 받기
n, m = map(int, input().strip().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

print(bfs_maze(maze, n, m))