#只遍历key而不便利value的方法
#格式：字典名.keys()
#keys()函数会返回字典中所有的key，而不返回value
#遍历key的方式其实是字典的默认行为，向数组那样遍历字典也会返回key
favourite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

for name in favourite_languages.keys():
	print(name.title())

#字典的默认行为
print("\n")
for name in favourite_languages:
	print(name)

print("\n")

#使用遍历出的key来访问字典
friends = ['phil', 'sarah']
for name in favourite_languages:
	print(name.title())
	if name in friends:
		print("Hi" + name.title() + 
			", I see your favourite language is " + favourite_languages[name].title())


if 'Erin' not in favourite_languages:
	print("Erin, please take our poll!")





