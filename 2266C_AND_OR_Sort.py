t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    if s[0] == "1":
        print(s.count("0"))
    else:
        a = s.count("0")
        b = 0
        c = a - 1
        ans = b + c
        for i in range(1, n):
            if s[i] == "1":
                b += 1
            else:
                c -= 1
            d = b + c
            if d < ans:
                ans = d
        print(ans)