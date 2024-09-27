# https://www.acmicpc.net/problem/1149

def dp(n):
    # 1. 테이블
    dt = [[0]*3 for _ in range(n+1)]

    # 2. 초기값
    dt[1][0] = r[1]
    dt[1][1] = g[1]
    dt[1][2] = b[1]

    # 3. 점화식
    for i in range(2, n+1):
        dt[i][0] = min(dt[i-1][1], dt[i-1][2]) + r[i]
        dt[i][1] = min(dt[i-1][0], dt[i-1][2]) + g[i]
        dt[i][2] = min(dt[i-1][0], dt[i-1][1]) + b[i]

    return min(dt[i][0], dt[i][1], dt[i][2])
    

n = int(input())
r = [0] * (n+1)
g = [0] * (n+1)
b = [0] * (n+1)

for i in range(1, n+1):
    r[i], g[i], b[i] = map(int, input().split())

print(dp(n))
