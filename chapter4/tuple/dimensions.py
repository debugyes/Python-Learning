#使用元组
#元组就是不可变的数组
#格式：元组名 = (元素)
#元组用() 数组用[]
#访问单个元素的方法和数组一样
#如果要改变元组的值只能重新定义元组

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#dimensions[0] = 250
#python不允许改变元组的元素值

for dimension in dimensions:
	print(dimension)


#重新定义元组，改变元组值
dimensions = [400, 100]
print("modified dimensions:")
for dimension in dimensions:
	print(dimension)