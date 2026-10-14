t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if b >= a:
        f0 = b - a
    else:
        f0 = max(0, a - b - c)
    fc = abs(a + c - b)
    print(max(f0, fc))