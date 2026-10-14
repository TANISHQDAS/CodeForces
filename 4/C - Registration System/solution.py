n = int(input())
db = {}
for _ in range(n):
    name = input().strip()
    if name not in db:
        db[name] = 0
        print("OK")
    else:
        db[name] += 1
        new_name = name + str(db[name])
        while new_name in db:
            db[name] += 1
            new_name = name + str(db[name])
        db[new_name] = 0
        print(new_name)