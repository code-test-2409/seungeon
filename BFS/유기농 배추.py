# https://www.acmicpc.net/problem/1012
# 연속된 배추 영역의 개수 구하기

from collections import deque

# 테스트 케이스 개수
T = int(input())

# 이동 방향 (상, 하, 좌, 우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):           
    queue = deque([(x,y)]) # 큐 초기화
    matrix[x][y] = 0 # 현재 위치 방문 처리

    while queue:
        x, y = queue.popleft(0)

        # 인접 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 인접 위치가 범위 내에 있고, 배추가 있는 경우
            if 0 <= nx < M and 0 <= ny < N and matrix[nx][ny] == 1:
                queue.append((nx, ny))
                matrix[nx][ny] = 0  # 방문 처리

# 각 테스트 케이스 처리
for i in range(T):
    M, N, K = map(int, input().split()) # 가로, 세로, 개수
    matrix = [[0] * N for _ in range(M)]
    cnt = 0 # 지렁이 수

    for _ in range(K):
        x, y = map(int, input().split())
        matrix[x][y] = 1

    for a in range(M):
        for b in range(N):
            if matrix[a][b] == 1:
                bfs(a, b)
                cnt += 1

    print(cnt)