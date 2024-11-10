def rabin_karp(s, length):
    n = len(s)
    if length == 0:
        return True
    
    base = 256
    mod = 2**61 - 1
    current_hash = 0
    highest_pow = 1
    
    for i in range(length):
        current_hash = (current_hash * base + ord(s[i])) % mod
        if i < length - 1:
            highest_pow = (highest_pow * base) % mod
    
    seen_hashes = {current_hash}
    
    for i in range(length, n):
        current_hash = (current_hash * base - ord(s[i - length]) * highest_pow + ord(s[i])) % mod
        if current_hash in seen_hashes:
            return True
        seen_hashes.add(current_hash)
    
    return False

def longest_repeated_substring_length(s):
    n = len(s)
    left, right = 0, n
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        if rabin_karp(s, mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result

# 입력 받기
L = int(input().strip())
s = input().strip()

# 결과 출력
print(longest_repeated_substring_length(s))