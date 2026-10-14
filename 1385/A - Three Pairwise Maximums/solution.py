t = int(input())
for _ in range(t):
    x, y, z = map(int, input().split())
    arr = sorted([x, y, z])
    if arr[1] != arr[2]:
        print("NO")
    else:
        print("YES")
        print(arr[0], arr[0], arr[2])