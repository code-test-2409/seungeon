import sys

input = sys.stdin.read

# 입력을 받아오기
data = input().strip().split()
index = 0

T = int(data[index])
index += 1

results = []

for _ in range(T):
    N = int(data[index])
    index += 1
    applicants = []
    
    for _ in range(N):
        doc_rank = int(data[index])
        int_rank = int(data[index + 1])
        applicants.append((doc_rank, int_rank))
        index += 2
    
    # 서류 심사 성적을 기준으로 정렬
    applicants.sort()

    # 면접 성적의 기준을 첫 번째 지원자의 면접 성적으로 설정
    max_interview_rank = applicants[0][1]
    count = 1
    
    for i in range(1, N):
        if applicants[i][1] < max_interview_rank:
            count += 1
            max_interview_rank = applicants[i][1]
    
    results.append(count)

for result in results:
    print(result)