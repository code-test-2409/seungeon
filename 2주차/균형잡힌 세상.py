import sys

input = sys.stdin.readline
results = []

while True:
    a = input().rstrip()  # 입력을 받고 줄바꿈 문자를 제거합니다.
    stack = []

    if a == '.':
        break

    for i in a:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()  # 맞으면 스택에서 제거
            else:
                stack.append(']')
                break
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
    
    if len(stack) == 0:
        results.append("yes")
    else:
        results.append("no")

print("\n".join(results))