# https://www.acmicpc.net/problem/2839

# 봉지 수를 최대한 적게
# 5로 나눠지는 경우 / 5+3 으로 나눠지는 경우 / 3으로 나눠지는 경우 / 나머지가 남는 경우

n = int(input()) # 3 <= 설탕의 양 n <= 5000)

if n % 5 == 0:
    print(n // 5)
else:
    bag = 0
    while n > 0:
        n -= 3 # n이 0보다 큰 동안, 3kg을 빼고 봉지 개수를 1 증가
        bag += 1 # 3kg 봉지
        if n % 5 == 0:
            bag += n
            print(bag)
            break
        elif n == 1 or n==2:
            print(-1)
            break
        else:
            print(bag)
            break
