#操作字典
#一个key：一个值
#每个key用逗号分隔
#操作单独一个key的方法：
#字典名[key]

#添加新的key进入字典
#字典名[key] = value
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned" + str(new_points) + "points")


#添加新的key-value-pair进字典
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)