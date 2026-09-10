y=int(input())
 
while True:
    y+=1
    s=str(y)
    if len(set(s))==4:
        print(y)
        break