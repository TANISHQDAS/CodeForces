t = int(input())
for _ in range(t):
    n = int(input())
    b = n.bit_length()
    s = 1 << b
    g = [i ^ (i >> 1) for i in range(s)]
    p = g + g
    a = [p[i] ^ p[i + 1] for i in range(len(p) - 1)]
    print(len(a))
    print(*a)
 