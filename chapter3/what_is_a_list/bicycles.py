#访问元素

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#单独处理每个元素
print(bicycles[0])
print(bicycles[0].title())

#索引是元素所在位置-1
print(bicycles[1])#第二个元素下标为1
print(bicycles[3])#第四个元素下标为3

#访问最后一个元素
print(bicycles[3])#方法一
print(bicycles[-1])#方法二，索引为-1时python返回最后一个元素
#举一反三，访问倒数第二个元素
print(bicycles[-2])
#访问倒数第三个元素
print(bicycles[-3])

#用数组中的元素来组成一段话
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)