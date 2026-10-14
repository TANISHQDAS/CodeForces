t = int(input())
for _ in range(t):
    n, m, d = map(int, input().split())
    h = d // m + 1
    print((n + h - 1) // h)