n = int(input())
a = list(map(int, input().split()))
sorted_a = sorted(a, reverse=True)
pos = {}
for i, val in enumerate(sorted_a):
    if val not in pos:
        pos[val] = i + 1
print(" ".join(str(pos[val]) for val in a))