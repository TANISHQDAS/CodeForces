n=input()
m=input()
o=[]
 
for i in range(len(n)):
    if n[i]==m[i]:
        o.append('0')
    else:
        o.append('1')
 
print(''.join(o))