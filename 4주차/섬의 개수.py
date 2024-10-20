import sys
from collections import deque

input = sys.stdin.readline

# 방향 벡터: 상, 하, 좌, 우, 좌상, 우상, 좌하, 우하
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(x, y, w, h, map_data):
    queue = deque([(x, y)])
    map_data[x][y] = 0  # 방문 처리

    while queue:
        cx, cy = queue.popleft()
        for d in range(8):  # 8 방향 탐색
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < h and 0 <= ny < w and map_data[nx][ny] == 1:
                map_data[nx][ny] = 0  # 방문 처리
                queue.append((nx, ny))

# 입력 처리 및 섬 개수 세기
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    map_data = [list(map(int, input().split())) for _ in range(h)]
    island_count = 0
    
    for i in range(h):
        for j in range(w):
            if map_data[i][j] == 1:  # 새로운 섬 발견
                bfs(i, j, w, h, map_data)
                island_count += 1

    print(island_count)
