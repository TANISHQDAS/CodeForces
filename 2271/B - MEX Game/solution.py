t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    c = [0] * (n + 2)
    for x in a:
        c[x] += 1
    ans = False
    for i in range(n + 2):
        if c[i] < 2 * k:
            ans = c[i] == 2 * k - 1
            break
    print("YES" if ans else "NO")