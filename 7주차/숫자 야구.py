import sys
input = sys.stdin.read

# 입력 읽기
data = input().split()
N = int(data[0])

# 질문 리스트 생성
questions = []
index = 1
for _ in range(N):
    guess = data[index]
    strikes = int(data[index + 1])
    balls = int(data[index + 2])
    questions.append((guess, strikes, balls))
    index += 3

possible_candidates = 0

# 가능한 모든 후보 숫자 생성 및 검증
for i in range(1, 10):
    for j in range(1, 10):
        if j == i:
            continue
        for k in range(1, 10):
            if k == i or k == j:
                continue
            candidate = f"{i}{j}{k}"
            
            valid = True
            for guess, expected_strikes, expected_balls in questions:
                strike = 0
                ball = 0
                
                # 스트라이크 및 볼 계산
                for x in range(3):
                    if candidate[x] == guess[x]:
                        strike += 1
                    elif candidate[x] in guess:
                        ball += 1
                        
                if strike != expected_strikes or ball != expected_balls:
                    valid = False
                    break
            
            if valid:
                possible_candidates += 1

print(possible_candidates)