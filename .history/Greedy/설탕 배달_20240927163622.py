# https://www.acmicpc.net/problem/2839

# 봉지 수 (몫)을 최대한 적게
# 우선순위 순으로
# 5로 나눠지는 경우 / 5+3 으로 나눠지는 경우 / 3으로 나눠지는 경우 / 나머지가 남는 경우

n = int(input())

if n % 5 == 0:
    print(n // 5)
    print(n / 5)