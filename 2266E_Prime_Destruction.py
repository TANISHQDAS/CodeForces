M = 200005
s = list(range(M))
for i in range(2, 450):
    if s[i] == i:
        for j in range(i * i, M, i):
            if s[j] == j:
                s[j] = i
 
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    p = [0] * (n + 1)
    for y in range(k + 1, n + 1):
        x = y
        m = 10**18
        while x > 1:
            d = s[x]
            v = 1 + d * p[y // d]
            if v < m:
                m = v
            while x % d == 0:
                x //= d
        p[y] = m
    print(sum(p[x] for x in a))