for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    p = [0] * (n + 1)
    for i in range(n):
        p[i + 1] = (p[i] + a[i]) % k
    c = [0] * k
    s = 0
    for r in range(k + 1, n + 1):
        c[p[r - k - 1]] += 1
        s += c[p[r]]
    print(s)