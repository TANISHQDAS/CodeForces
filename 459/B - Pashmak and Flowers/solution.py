n = int(input())
flowers = list(map(int, input().split()))
 
max_b = max(flowers)
min_b = min(flowers)
max_diff = max_b - min_b
 
if max_diff == 0:
    # All flowers are the same
    ways = n * (n - 1) // 2
else:
    count_max = flowers.count(max_b)
    count_min = flowers.count(min_b)
    ways = count_max * count_min
 
print(max_diff, ways)