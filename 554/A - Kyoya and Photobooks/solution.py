s = input().strip()
n = len(s)
ans = set()
for i in range(n + 1):
    for ch in 'abcdefghijklmnopqrstuvwxyz':
        ans.add(s[:i] + ch + s[i:])
print(len(ans))