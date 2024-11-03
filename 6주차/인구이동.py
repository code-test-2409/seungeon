import sys
from collections import deque

input = sys.stdin.read
data = input().split()
index = 0

N = int(data[index])
L = int(data[index + 1])
R = int(data[index + 2])
index += 3

pan = []
for i in range(N):
    pan.append([int(data[index + j]) for j in range(N)])
    index += N

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    union = [(x, y)]
    while q:
        a, b = q.popleft()
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            if 0 <= na < N and 0 <= nb < N and not visited[na][nb]:
                if L <= abs(pan[a][b] - pan[na][nb]) <= R:
                    visited[na][nb] = True
                    q.append((na, nb))
                    union.append((na, nb))
    if len(union) > 1:
        total_population = sum(pan[a][b] for a, b in union)
        new_population = total_population // len(union)
        for a, b in union:
            pan[a][b] = new_population
        return True
    return False

day = 0
while True:
    visited = [[False] * N for _ in range(N)]
    stop = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                if bfs(i, j):
                    stop = True
    if not stop:
        break
    day += 1

print(day)