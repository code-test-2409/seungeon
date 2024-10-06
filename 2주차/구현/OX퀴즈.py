def calculate_score(result):
    score = 0
    consecutive_o = 0
    
    for char in result:
        if char == 'O':
            consecutive_o += 1
            score += consecutive_o
        else:
            consecutive_o = 0
    
    return score

test_cases = int(input().strip())
results = [input().strip() for _ in range(test_cases)]

for result in results:
    print(calculate_score(result))