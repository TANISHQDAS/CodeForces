t = int(input())
 
for _ in range(t):
    n = int(input())
    s = input().strip()
 
    st = []
    p = [False] * (n + 1)
 
    for i in range(1, n + 1):
        if s[i - 1] == '1':
            st.append(i)
        elif s[i - 1] == '2':
            if st:
                x = st.pop()
                p[x] = True
            else:
                p[i] = True
        else:
            p[i] = True
 
    a = []
 
    for i in range(1, n + 1):
        if not p[i]:
            a.append(i)
 
    print(len(a))
    print(*a)