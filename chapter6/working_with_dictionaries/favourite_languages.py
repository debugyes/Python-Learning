#添加同一类不同物体内容的字典
favourite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

print("sarah's favourite language is " + favourite_languages['sarah'].title() + ".")

for name, language in favourite_languages.items():
	print("name:" + name)
	print("favourite language:" + language + "\n")
