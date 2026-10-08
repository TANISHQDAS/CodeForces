t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = n - 4
    v = []
    for i in range(m):
        v.append(a[i] + a[i + 2] - a[i + 4])
    d = {}
    for x in v:
        d[x] = d.get(x, 0) + 1
    s = 0
    for c in d.values():
        s += c * (c - 1) // 2
    for i in range(m):
        if i + 2 < m and v[i] == v[i + 2]:
            s -= 1
        if i + 4 < m and v[i] == v[i + 4]:
            s -= 1
    print(s)