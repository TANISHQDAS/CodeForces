t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(set(a[i] - (i + 1) for i in range(n)))
    s = 1
    c = 1
    for i in range(1, len(b)):
        if b[i] == b[i - 1] + 1:
            c += 1
        else:
            c = 1
        if c > s:
            s = c
    print(s)