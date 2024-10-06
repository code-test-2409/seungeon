def alphabet(word):
    # 1. 모든 문자를 대문자로 변환
    word = word.upper()
    
    # 2. 빈도수 계산
    frequency = {}
    for char in word:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
            
    # 3. 가장 많이 사용된 알파벳 찾기
    max_freq = max(frequency.values())
    most_frequent = [key for key, value in frequency.items() if value == max_freq]
    
    if len(most_frequent) > 1:
        return "?"
    else:
        return most_frequent[0]

# 예제 입력
word = input().strip()
print(alphabet(word))