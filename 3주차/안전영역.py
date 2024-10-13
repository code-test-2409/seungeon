from collections import deque

# 입력
n = int(input())
graph = []
max_height = 0

# 그래프 입력과 동시에 최대 높이 찾기
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    max_height = max(max_height, max(row))

# 상하좌우 방향 벡터 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# (x, y) 지점에서 시작하여 연결된 안전한 영역을 탐색
def bfs(x, y, rain_level, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] > rain_level:
                visited[nx][ny] = True
                queue.append((nx, ny))

# 안전한 영역의 최대 개수 찾기
result = 0
for rain_level in range(max_height):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > rain_level and not visited[i][j]:
                bfs(i, j, rain_level, visited)
                count += 1
    result = max(result, count)

print(result)