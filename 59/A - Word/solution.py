txt = input()
low = sum(i.islower() for i in txt)
up = len(txt) - low
print(txt.lower() if low >= up else txt.upper())