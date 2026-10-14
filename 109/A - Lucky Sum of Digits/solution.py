n = int(input())
found = False
for y in range(n // 7, -1, -1):
    x = n - 7 * y
    if x % 4 == 0:
        x //= 4
        print("4" * x + "7" * y)
        found = True
        break
if not found:
    print(-1)