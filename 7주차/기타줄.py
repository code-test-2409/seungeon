n, m = map(int, input().split())

# 초기화
min_package_price = float('inf')
min_individual_price = float('inf')

# 입력 받아서 최소 가격 계산
for _ in range(m):
    package_price, individual_price = map(int, input().split())
    if package_price < min_package_price:
        min_package_price = package_price
    if individual_price < min_individual_price:
        min_individual_price = individual_price

# 최소 비용 계산
cost_only_packages = (n // 6) * min_package_price + (n % 6) * min_individual_price
cost_mixed = (n // 6 + 1) * min_package_price
cost_only_individuals = n * min_individual_price

min_cost = min(cost_only_packages, cost_mixed, cost_only_individuals)

print(min_cost)