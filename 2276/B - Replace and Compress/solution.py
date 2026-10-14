for _ in range(int(input())):
    s = input().strip()
    b = 1
    x = y = 0
    for i in range(1, len(s) - 1):
        if s[i-1] == s[i] == s[i+1]:
            x = 1
        if s[i-1] == s[i+1] != s[i]:    
            y = 1
    print(b + x + y)