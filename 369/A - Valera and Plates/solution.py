n, m, k = map(int, input().split())
dishes = list(map(int, input().split()))
wash = 0
for dish in dishes:
    if dish == 1:
        if m > 0:
            m -= 1
        else:
            wash += 1
    else:
        if k > 0:
            k -= 1
        elif m > 0:
            m -= 1
        else:
            wash += 1
print(wash)