n, m = map(int, input().split())
tasks = list(map(int, input().split()))
pos = 1
time = 0
for t in tasks:
    if t >= pos:
        time += t - pos
    else:
        time += n - (pos - t)
    pos = t
print(time)