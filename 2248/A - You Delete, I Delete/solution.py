t = int(input())
for _ in range(t):
    s = list(input())
    i = s.index('0')
    del s[i]
    j = s.index('1')
    del s[j]
    print(''.join(s))