import sys
import copy

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

office = []
index = 2
for i in range(N):
    office.append([int(data[index + j]) for j in range(M)])
    index += M

# 각 CCTV의 방향 설정
cctv_directions = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]

# 이동 방향 (우, 하, 좌, 상)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# CCTV의 위치 저장
cctvs = []
for i in range(N):
    for j in range(M):
        if 1 <= office[i][j] <= 5:
            cctvs.append((i, j, office[i][j]))

# 주어진 방향으로 감시 진행
def watch(x, y, direction, temp_office):
    for d in direction:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or temp_office[nx][ny] == 6:
                break
            if temp_office[nx][ny] == 0:
                temp_office[nx][ny] = 9

# 백트래킹을 통해 모든 경우의 수를 탐색
def dfs(depth, office):
    global min_blind_spot
    
    if depth == len(cctvs):
        blind_spot = sum(row.count(0) for row in office)
        min_blind_spot = min(min_blind_spot, blind_spot)
        return
    
    x, y, cctv_type = cctvs[depth]
    for direction in cctv_directions[cctv_type]:
        temp_office = copy.deepcopy(office)
        watch(x, y, direction, temp_office)
        dfs(depth + 1, temp_office)

min_blind_spot = N * M
dfs(0, office)
print(min_blind_spot)