for _ in range(int(input())):
    n, m = map(int, input().split())
    if n == 1:
        print(0)
    else:
        a = (n + 1) // 2
        print(a)
        for i in range(1, a + 1):
            print(i, i + a - 1)