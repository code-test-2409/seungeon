def minimum_steps_to_return_books(N, M, positions):
    positions.sort()
    
    total_steps = 0

    # 책을 왼쪽에서 가져올 경우
    leftmost = positions[0]
    rightmost = positions[-1]
    
    # 왼쪽 책 처리
    if leftmost < 0:
        # 음수 좌표에서 책을 가져오는 경우
        for i in range(N // M):
            total_steps += abs(leftmost) * 2  # 왼쪽에서 가장 먼 책으로 가고 다시 돌아오기
        if N % M != 0:
            total_steps += abs(leftmost)  # 남은 책이 있을 경우 한 번만 가고 돌아옴
    
    # 오른쪽 책 처리
    if rightmost > 0:
        # 양수 좌표에서 책을 가져오는 경우
        for i in range(N // M):
            total_steps += rightmost * 2  # 오른쪽에서 가장 먼 책으로 가고 다시 돌아오기
        if N % M != 0:
            total_steps += rightmost  # 남은 책이 있을 경우 한 번만 가고 돌아옴
    
    return total_steps

# 입력
N, M = map(int, input().split())
positions = list(map(int, input().split()))

# 결과 출력
print(minimum_steps_to_return_books(N, M, positions))