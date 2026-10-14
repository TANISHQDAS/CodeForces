n = int(input())
a = sorted(map(int, input().split()), reverse=True)
s = sum(a)
x = 0
c = 0
for i in a:
    x += i
    c += 1
    if x > s - x:
        break
print(c)