t = int(input())
 
for _ in range(t):
    x0, y0, r = map(int, input().split())
 
    for dx in range(-r, r + 1):
        for dy in range(-r, r + 1):
            if dx * dx + dy * dy == r * r:
                print(x0 + dx, y0 + dy)
                break
        else:
            continue
        break