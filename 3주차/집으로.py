import math

# 입력
X, Y, D, T = map(int, input().split())

# 현재 위치에서 집까지의 유클리드 거리
distance = math.sqrt(X ** 2 + Y ** 2)

# 걷기만 사용할 경우
min_time = distance  # 초기값: 걷기만 사용할 때의 시간

# 점프를 사용하는 경우
max_jumps = int(distance // D) + 1  # 최대 점프 횟수

for k in range(max_jumps + 1):
    jump_distance = k * D  # k번 점프했을 때 이동한 거리
    remaining_distance = max(0, distance - jump_distance)  # 남은 거리
    time_for_jumps = k * T  # 점프하는 데 걸리는 시간
    
    total_time = time_for_jumps + remaining_distance

    min_time = min(min_time, total_time)

print(f"{min_time:.10f}")