n = input().strip()
length = len(n)
index = (1 << length) - 2
for i, ch in enumerate(n):
    if ch == '7':
        index += (1 << (length - i - 1))
print(index + 1)