#在数组中使用循环
#if 数组名：:
#用来检查数组中是否为空，如果至少有一个元素则返回true，如果为空则返回false
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

if requested_toppings:
	for requested_topping in requested_toppings:
		if requested_topping == 'green peppers':
			print("Sorry, we're out of green peppers right now")
		else:
			print("Adding " + requested_topping + ".")
else:
	print("Are you sure you want a plain pizza?")
print("\nfinished making my pizza")


#检查所需的配料是否合理
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni',
					 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding" + requested_topping + '.')
	else:
		print("Sorry, we don't have " + requested_topping` + ".")
print("\nFinished making your pizza")