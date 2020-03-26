#创建数字数组
#使用range()来生成一串连续的数字
#使用方法：range(起始数字，终止数字， 步长)
#range生成的一系列数字中不会出现终止数字

#可以通过将range生成的一串数字放在list的实参列表中来生成一个数字数组
#格式:数组名 = list(range(起始数字，终止数字))


for value in range(1, 5):
	print(value)

numbers = list(range(1, 6))

print(numbers)