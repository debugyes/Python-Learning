#在空字典中添加key-value-pair

#在字典中删除一个key的方法
#del 字典名[key]
#注意del是永久删除

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

#修改字典中的值
#字典名[key] = value
print("The alien is " + alien_0['color'])
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'])

#另一个例子
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original X position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("The new x position:" + str(alien_0['x_position']))

#从字典中删除一个key
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)