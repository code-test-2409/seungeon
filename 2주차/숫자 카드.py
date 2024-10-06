import sys

input = sys.stdin.readline

# 첫 줄: 상근이가 가진 숫자 카드의 개수
N = int(input().strip())

# 둘째 줄: 상근이가 가진 숫자 카드 목록
cards = set(map(int, input().strip().split()))

# 셋째 줄: 확인해야 할 숫자 카드의 개수
M = int(input().strip())

# 넷째 줄: 확인해야 할 숫자 카드 목록
query_num = list(map(int, input().strip().split()))

# 결과리스트
results = []
for number in query_num:
    if number in cards:
        results.append('1')
    else:
        results.append('0')

# 결과 출력
print(' '.join(results))