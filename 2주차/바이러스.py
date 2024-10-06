def dfs(graph, start, visited):
    stack = [start]
    count = 0
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            count += 1
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    stack.append(neighbor)
    return count - 1  # 1번 컴퓨터를 제외한 수를 반환

# 입력 받기
n = int(input().strip())  # 컴퓨터의 수
m = int(input().strip())  # 네트워크 상에서 직접 연결된 컴퓨터 쌍의 수
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)

# 방문 여부 리스트
visited = [False] * (n + 1)

# 1번 컴퓨터에서 시작하여 바이러스 전파
result = dfs(graph, 1, visited)
print(result)