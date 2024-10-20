import sys

# 입력을 표준 입력에서 받아오기
input = sys.stdin.read

data = input().strip().split()
case_number = 1
i = 0

# 결과를 저장할 리스트
results = []

while i < len(data):
    # 각 테스트 케이스의 L, P, V 값을 읽어오기
    L = int(data[i])
    P = int(data[i+1])
    V = int(data[i+2])

    # 0 0 0이 입력된 경우 종료
    if L == 0 and P == 0 and V == 0:
        break

    # 최대 사용할 수 있는 날 계산
    full_periods = V // P
    remaining_days = V % P

    # 각 주기에서 최대 L일을 사용할 수 있고, 남은 일수에서 최대한 많이 사용
    max_days = full_periods * L + min(remaining_days, L)
    results.append(f"Case {case_number}: {max_days}")

    case_number += 1
    i += 3

# 결과 출력
for result in results:
    print(result)