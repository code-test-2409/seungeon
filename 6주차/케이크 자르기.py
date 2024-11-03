import sys
input = sys.stdin.read

def can_cut(cut_points, L, cuts, min_length):
    current = 0
    count = 0
    for point in cut_points:
        if point - current >= min_length:
            current = point
            count += 1
            if count == cuts:
                break
    return count >= cuts and (L - current >= min_length)

def find_max_min_length(cut_points, L, cuts):
    left, right = 1, L
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        if can_cut(cut_points, L, cuts, mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return result

data = input().split()

N = int(data[0])
M = int(data[1])
L = int(data[2])

cut_points = [int(data[i]) for i in range(3, 3 + M)]
cut_points.sort()

Q_list = [int(data[i]) for i in range(3 + M, 3 + M + N)]

results = []
for Q in Q_list:
    results.append(find_max_min_length(cut_points, L, Q))

for result in results:
    print(result)