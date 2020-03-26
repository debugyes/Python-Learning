#通过key-value-pair循环遍历一个数组
#数组名.items()返回一系列key-value-pairs
#for循环格式：for 变量1, 变量2 in 字典名.items():
#items()会返回一系列key-value-pairs，并将key存储到变量1，value存储到变量2

user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
}

for key, value in user_0.items():
	print("\nkey:" + key)
	print("\nvalue:" + value)