text=input().strip()
numbers=text.split("+")
numbers.sort()
# this will not sort for big numbers. e.g: 43 in ['', '3', '4', '42', '5', '8', '9']
numbers = list(filter(None, numbers))
count = len(numbers)
# print(numbers)
i=0
for num in numbers:
	print(num, end = '')
	if i != count-1:
		print("+", end = '')
	i+=1