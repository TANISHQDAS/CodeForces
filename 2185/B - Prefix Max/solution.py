t = int(input())
 
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
 
    best = 0
 
    for i in range(n):
        for j in range(i, n):
            temp = arr[:]
            temp[i], temp[j] = temp[j], temp[i]
 
            current_max = 0
            total = 0
 
            for value in temp:
                if value > current_max:
                    current_max = value
                total += current_max
 
            if total > best:
                best = total
 
    print(best)