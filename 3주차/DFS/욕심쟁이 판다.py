def dfs(x, y):
    if dp[x][y] != -1:  # 이미 방문한 경우
        return dp[x][y]
    
    # 현재 위치에서 이동할 수 있는 최대 칸 수
    max_steps = 1
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < n and 0 <= ny < n and bamboo[nx][ny] > bamboo[x][y]:
            max_steps = max(max_steps, 1 + dfs(nx, ny))
    
    dp[x][y] = max_steps
    return max_steps

n = int(input())
bamboo = [list(map(int, input().split())) for _ in range(n)]

# 방향 정의 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 배열 초기화
dp = [[-1] * n for _ in range(n)]

max_count = 0

# 모든 위치에서 DFS
for i in range(n):
    for j in range(n):
        max_count = max(max_count, dfs(i, j))

print(max_count)