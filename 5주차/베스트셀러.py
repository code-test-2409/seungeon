import sys
input = sys.stdin.readline

n = int(input())
book = {}

for i in range(n):
    name = input()
    if name not in book:
        book[name] = 1
    else:
        book[name] += 1
        
max_value = max(book.values())

bestseller = []
for key, value in book.items():
    if value == max_value:
        bestseller.append(key)

bestseller = sorted(bestseller)
print(bestseller[0])