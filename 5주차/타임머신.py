import sys
input = sys.stdin.readline
INF = int(1e9)

def bellman_ford(start):
    dist[start] = 0

    # n번의 라운드를 반복
    for i in range(1, n + 1):
        # 라운드마다 모든 간선을 확인
        for j in range(m):
            now, next, cost = edges[j][0], edges[j][1], edges[j][2]
            if dist[now] != INF and dist[next] > dist[now] + cost:
                dist[next] = dist[now] + cost
                if i == n:
                    return True

    return False

n, m = map(int, input().split())
edges = []
dist = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

negative_cycle = bellman_ford(1)

if negative_cycle:
    print(-1)
else:
    for i in range(2, n + 1):
        # 도달할 수 없는 경우
        if dist[i] == INF:
            print(-1)
        # 도달 가능한 경우
        else:
            print(dist[i])