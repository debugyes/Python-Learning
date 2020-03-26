#将一个数组复制到另一个数组中
#我们使用		新数组 = 旧数组[:]的方法
#[:] 省略开始索引和终止索引，形成包含整个数组的索引，再将这个片段给新的数组
#注意：如果直接将新数组 = 旧数组，那么就会造成两个数组名同时指向一个数组，操作一个数组名同时也是操作另一个数组名
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)