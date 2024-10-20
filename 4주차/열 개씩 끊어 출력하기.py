# 단어 입력 받기
word = input().strip()

# 단어의 길이
length = len(word)

# 10글자씩 끊어서 출력
for i in range(0, length, 10):
    print(word[i:i+10])