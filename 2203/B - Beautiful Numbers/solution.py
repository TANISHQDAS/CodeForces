t = int(input())
for _ in range(t):
    x = input().strip()
    
    s = sum(int(c) for c in x)
    if s <= 9:
        print(0)
        continue
    
    need = s - 9
    gains = []
    
    for i, c in enumerate(x):
        d = int(c)
        if i == 0:
            gains.append(d - 1)
        else:
            gains.append(d)
    
    gains.sort(reverse=True)
    
    moves = 0
    cur = 0
    for g in gains:
        cur += g
        moves += 1
        if cur >= need:
            break
    
    print(moves)