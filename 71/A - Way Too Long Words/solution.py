for _ in range(int(input())):
    x = input()
    t = len(x)
    
    if t > 10:
        print(f"{x[0]}{t - 2}{x[-1]}")
    else:
        print(x)