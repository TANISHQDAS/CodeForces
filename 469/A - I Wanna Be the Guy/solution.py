n = int(input())
x = list(map(int, input().split()))[1:]
y = list(map(int, input().split()))[1:]
print("I become the guy." if len(set(x + y)) == n else "Oh, my keyboard!")