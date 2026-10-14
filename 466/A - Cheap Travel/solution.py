n, m, a, b = map(int, input().split())
print(min((n // m) * b + min((n % m) * a, b), n * a))