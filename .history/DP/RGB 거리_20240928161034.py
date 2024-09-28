# https://www.acmicpc.net/problem/1149

def dp(n, costs):
    # 1. 테이블
    dp = [[0]*3 for _ in range(n)]

    # 2. 초기값
    dp[0] = costs[0]

    # 3. 점화식
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

    # 마지막 집의 최소 색칠 비용
    return min(dp[n-1])
    
n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]

print(dp(n, costs))
