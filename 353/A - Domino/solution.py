n = int(input())
upper, lower = 0, 0
dominoes = []
for _ in range(n):
    a, b = map(int, input().split())
    upper += a
    lower += b
    dominoes.append((a, b))
 
if upper % 2 == 0 and lower % 2 == 0:
    print(0)
elif upper % 2 == 1 and lower % 2 == 1:
    found = any((a % 2 != b % 2) for a, b in dominoes)
    print(1 if found else -1)
else:
    print(-1)