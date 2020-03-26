#使用if elif else
age = 12
if age < 4:
	print("your admission cost is $0")
elif age < 18:
	print("your admission cost is $5")
else:
	print("your admission cost is $10")

#更简洁的写法
age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
else:
	price = 5

print("your admission cost is $" + str(price) + ".")